import cv2
import numpy as np
from moviepy.editor import *

height = 384
width = 512

mie_pic = cv2.imread(r'E:\Python\badapple\mie2016.png')
videopath = 'E:\\Python\\badapple\\1.flv'

def fl(gf, t):
    img = gf(t)
    temp = np.array(img)
    # for i in range(height):
    #     for j in range(width):
    #         temp[i, j] = ~img[i, j]
    return cv2.bitwise_and(temp, mie_pic)

clip = VideoFileClip(videopath)
newclip = clip.fl(fl)
newclip.write_videofile('badmie_1.mp4')
