import numpy as np
import imageio
import scipy.ndimage
import cv2
img="that.jpg"
def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
    #2 dimensoon array formula to convert image to gray scale
def dodge(front,back):
    final_sketch=front*255/(255-back)
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255
    return final_sketch.astype('uint8')
ss=imageio.imread(img) #for read the given image
gray= rgb2gray(ss)
i=255-gray
blur=scipy.ndimage.filters.gaussian_filter(i, sigma=15)
#sigma is the intensity of blurness of image
r=dodge(blur,gray) #convert image to sketch
cv2.imwrite('virat-sketch.png', r)