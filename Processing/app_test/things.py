#########################################################

old_state = []
for i in range(len(state)):
    if state[i]:
        old_state.append("empty")
    else:
        old_state.append("occupied")

#########################################################

img_color = cv2.imread(test,cv2.IMREAD_COLOR)
img_color = cv2.cvtColor(img_color,cv2.COLOR_BGR2RGB)
green = np.uint8([[[0,255,0 ]]])
red = np.uint8([[[255,0,0]]])

for i in range(len(coords)-14):
    if meh2[i]:
        color = (0,255,0)
    else:
        color = (255,0,0)
    cv2.line(img_color, coords[i][3], coords[i][0], color, thickness=2, lineType=8, shift=0)
    cv2.line(img_color, coords[i][0], coords[i][1], color, thickness=2, lineType=8, shift=0)
    cv2.line(img_color, coords[i][1], coords[i][2], color, thickness=2, lineType=8, shift=0)
    cv2.line(img_color, coords[i][2], coords[i][3], color, thickness=2, lineType=8, shift=0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    
#     cv2.putText(img_color,str(i+1),coords[i][0], font, 0.4,(0,0,255),1,cv2.LINE_AA)

img_color = cv2.cvtColor(img_color,cv2.COLOR_RGB2BGR)
cv2.imwrite('test_out4.jpg',img_color)
img_color = cv2.cvtColor(img_color,cv2.COLOR_BGR2RGB)
plt.figure(figsize=(16,16))
plt.imshow(img_color)
plt.show()

#########################################################

img1 = cv2.imread("back_test/1.jpg",cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("back_test/2.jpg",cv2.IMREAD_GRAYSCALE)

fgbs = cv2.bgsegm.createBackgroundSubtractorMOG()
a = fgbs.apply(img2)
diff = img2-img1
sq=np.ones((5,5))

# plt.figure(figsize=(16,16))
# plt.subplot(2,2,1)
# plt.imshow(img1,cmap="gray")
# plt.subplot(2,2,2)
# plt.imshow(img2,cmap="gray")
# plt.subplot(2,2,3)
# plt.imshow(diff,cmap="gray")
# plt.subplot(2,2,4)
# plt.imshow(fgbs.apply(img1),cmap="gray")
# plt.show()

#########################################################

img = cv2.imread('new3.jpg',cv2.IMREAD_COLOR)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
test = 'test5.jpg'
img2 = cv2.imread(test,cv2.IMREAD_COLOR)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
pklot_empty = obtain_pklots(img,coords,coordsX,coordsY)
pklot_new = obtain_pklots(img2,coords,coordsX,coordsY)

#########################################################

#########################################################

#########################################################

#########################################################

#########################################################

#########################################################

#########################################################

#########################################################

#########################################################

#########################################################





