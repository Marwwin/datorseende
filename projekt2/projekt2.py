#%%
import matplotlib.pyplot as plt
import matplotlib.image as img 
import numpy as np
import cv2
import os

def processImg(input,showHist =False):
  img_temp = img.imread("thumbnail/"+input)
  img_np =  np.int_(img_temp*255)
  img_equ = cv2.equalizeHist(img_temp)
  clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8,8))
  img_clahe = clahe.apply(img_temp)

  if showHist:
    print("Image:"+input)
    plt.figure(figsize=(16,6))

    plt.subplot(1,3,1)
    plt.hist(img_np.flatten(),256,[0,256], color = 'r', label="Original Image") 
    plt.legend()
    
    plt.subplot(1,3,2)
    plt.hist(img_equ.flatten(),256,[0,256],color = 'g', label="Equalized Histogram")
    plt.legend()

    plt.subplot(1,3,3)
    plt.hist(img_clahe.flatten(),256,[0,256], color = 'b', label="CLAHE Histogram") 
    plt.legend()
    plt.show()
  return {"np":img_np,"og": img_temp, "eq":img_equ,"cl":img_clahe}

def showImg(input):
  print(input["og"],input["eq"],input["cl"])
  stacked_img = np.hstack((input["og"],input["eq"],input["cl"]))
  plt.show()
  cv2.namedWindow("main", cv2.WINDOW_NORMAL)
  cv2.imshow("main",stacked_img)
  cv2.waitKey(0)
  cv2.waitKey(0)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def loadImages():
  imgFiles = os.listdir("thumbnail/")
  imgList = []
  for i in imgFiles:
    imgList.append(processImg(i,True))
  return imgList

theList = loadImages()


#%%
#def showImg2(input):
#  print(input["og"],input["eq"],input["cl"])
#  stacked_img = np.hstack((input["og"],input["eq"],input["cl"]))
#  plt.figure(figsize=(16,6))
#  plt.imshow(stacked_img, cmap="gray")
#
#showImg2(theList[0])

#%%


#%%


def processImg2(input,showHist =False):
  #img_temp = img.imread("p2img/"+input)
  #img_temp = (img_temp[0]+img_temp[1]+img_temp[2])//3
  img_np =  np.int_(input).astype(np.uint8)
  img_equ = cv2.equalizeHist(input)
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4,4))
  img_clahe = clahe.apply(input)

  if showHist:
  
    plt.hist(img_np.flatten(),256,[0,256], color = 'r') 
    plt.show()
    plt.hist(img_equ.flatten(),256,[0,256],color = 'g')
    plt.show()
    plt.hist(img_clahe.flatten(),256,[0,256], color = 'b') 
    plt.show()

  return {"np":img_np,"og": input, "eq":img_equ,"cl":img_clahe}


im = img.imread("bathroom.jpg")
gim = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
pImg = processImg2(gim,True)
showImg(pImg)

