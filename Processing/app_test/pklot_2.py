import cv2
import numpy as np
from skimage.measure import compare_ssim
from os import listdir, path
from tempfile import TemporaryFile
import pymysql
import argparse


def connect_db(sql,action):
    
    r=[]
    if action == "u":
        cursor.execute(sql)
        db.commit()
    if action == "s":
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            r.append(row)
        return r

def obtain_pklots(entry,coords,coordsX,coordsY):
    masks = []
    image = entry
    for i in range(len(coords)):
        ROI_corners = np.array([coords[i].tolist()], dtype=np.int32) 
        mask = np.zeros(image.shape, dtype=np.uint8)
        cv2.fillPoly(mask, ROI_corners, (255))
        masked_image = cv2.bitwise_and(image, mask)
        masked_image = masked_image[np.min(coordsY[i]):np.max(coordsY[i]),np.min(coordsX[i]):np.max(coordsX[i])]
        masks.append(masked_image)
    return masks

def read_images(path):
    img_list   = {}
    img_clist  = {}
    files_imgs = sorted(listdir(path))
    cont       = 0
#     print(files_imgs)
    for i in files_imgs:
        img_clist[str(cont)] = cv2.imread(path+'/'+i,cv2.IMREAD_COLOR)
        img_list[str(cont)] = cv2.imread(path+'/'+i,cv2.IMREAD_GRAYSCALE)
        cont = cont + 1
    
    return [img_list,img_clist]



def compare(pklot_empty,pklot_ref,pklot_new,state_old):
    scores     = []
    scores_emp = []
    bck_diff   = []
    stat       = []
    for i in range(len(pklot_ref)): 
        
        img_emp = pklot_empty[i]
        img_A   = pklot_ref[i]
        img_B   = pklot_new[i]

        bck_diff.append(img_B-img_A)

        
        (score_emp,_) = compare_ssim(img_emp, img_B, full=True)
        (score,_)     = compare_ssim(img_A, img_B, full=True)
        score         = np.float32(score)
        
        scores.append(score)
        scores_emp.append(score_emp)
        
        if score > 0.65 :
            stat.append(state_old[i])
        else:
            
            if state_old[i] == "occupied":
                if score_emp < 0.6:
                    stat.append("occupied")
                else:
                    stat.append("empty")
            else:
                stat.append("occupied")
                
    
    
    return [scores_emp,scores,stat]


def show_pklots(img_color,coords,state):
    #img_color = cv2.cvtColor(img_color,cv2.COLOR_BGR2RGB)
    
    for i in range(len(coords)-14):
        if state[i] == "empty":
            color = (0,255,0)
        else:
            color = (0,0,255)
#         cv2.line(img_color, coords[i][3], coords[i][0], color, thickness=2, lineType=8, shift=0)
#         cv2.line(img_color, coords[i][0], coords[i][1], color, thickness=2, lineType=8, shift=0)
#         cv2.line(img_color, coords[i][1], coords[i][2], color, thickness=2, lineType=8, shift=0)
#         cv2.line(img_color, coords[i][2], coords[i][3], color, thickness=2, lineType=8, shift=0)
        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(img_color,str(i),coords[i][0], font, 0.4,color,1,cv2.LINE_AA)

    cv2.imshow("Parkinglot",img_color)
    cv2.waitKey(0)


#Lectura de las imagenes
imgs,imgsc = read_images("ssim_test/day1")

#Loop de deteccion
state = np.load("state.npy").tolist()
pklot_empty = np.load("pklot_empty.npy")
coords = np.load("coords.npy")
coordsX = np.load("coordsX.npy")
coordsY = np.load("coordsY.npy")

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--ind', dest='ind', action='store', type=int,
                    help='The number of the image')

args = parser.parse_args()

ind = args.ind

# for i in range(10):
pklot_old = obtain_pklots(imgs[str(ind-1)],coords,coordsX,coordsY)
pklot_new = obtain_pklots(imgs[str(ind)],coords,coordsX,coordsY)
comp_e,comp,temp = compare(pklot_empty,pklot_old,pklot_new,state[ind-1])
state.append(temp)
# state[ind] = temp
show_pklots(imgsc[str(ind)],coords,state[ind])
np.save("state.npy", state)
#print(state[ind])