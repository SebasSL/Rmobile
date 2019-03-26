import cv2
import numpy as np
from skimage.measure import compare_ssim
from os import listdir, path
from tempfile import TemporaryFile
import pymysql


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


#Lectura de las coordenadas
db = pymysql.connect("localhost","sebRM","sebrm","Rumbomobile")
cursor = db.cursor()

pklot_dbname = "pklot2"

sql = "SELECT * FROM "+pklot_dbname
data = connect_db(sql,"s")

#Acondicionamiento de las coordenadas para su uso

coordsX=[]
b=[coordsX.append(data[i][1].split(",")) for i in range(len(data))]
coordsY=[]
b=[coordsY.append(data[i][2].split(",")) for i in range(len(data))]

coordsX = np.float32(coordsX)
coordsY = np.float32(coordsY)
coords = np.zeros(coordsX.shape,dtype = tuple)
coords_mag = np.sqrt(coordsX**2 + coordsY**2)
coords_mag.sort()
minmag = coords_mag[:,0]
maxmag = coords_mag[:,3]

for i in range(len(coordsX)):
    k = 1
    for j in range(len(coordsX[1])):
        
        if (np.abs(np.sqrt(coordsX[i][j]**2 + coordsY[i][j]**2) - minmag[i]) <=0.01):
            coords[i][0]=(coordsX[i][j],coordsY[i][j])
        elif (np.abs(np.sqrt(coordsX[i][j]**2 + coordsY[i][j]**2) - maxmag[i]) <=0.01):
            coords[i][2]=(coordsX[i][j],coordsY[i][j])
        else:
            coords[i][k]=(coordsX[i][j],coordsY[i][j])
            k = k + 2
        
            
coords.tolist();
coordsX = np.uint16(coordsX)
coordsY = np.uint16(coordsY)

#Lectura de las imagenes
imgs,imgsc = read_images("ssim_test/day1")

#Primera deteccion

img = cv2.imread('new3.jpg',cv2.IMREAD_GRAYSCALE)

pklot_empty = obtain_pklots(img,coords,coordsX,coordsY)
pklot_new = obtain_pklots(imgs["0"],coords,coordsX,coordsY)
state = []
comp = []
ms = []
bck_diff = []
for i in range(len(pklot_empty)): 

    img_A = pklot_empty[i]
    img_B = pklot_new[i]
    
    bck_diff.append(img_B-img_A)
    
    (score, diff) = compare_ssim(img_A, img_B, full=True)
    comp.append(score)
    
comp = np.float32(comp)
# print(compare)
meh2= (comp>0.5)
comp.sort()
# print(compare)
# print(meh2)
old_state = []
for i in range(len(meh2)):
    if meh2[i]:
        old_state.append("empty")
    else:
        old_state.append("occupied")
        
pklot_old = pklot_new
state.append(old_state)
np.save("state.npy", state)
np.save("pklot_empty.npy", pklot_empty)
np.save("coords.npy", coords)
np.save("coordsX.npy", coordsX)
np.save("coordsY.npy", coordsY)
