import cv2
import numpy as np
from moviepy.editor import *

height = 384
width = 512

mie_pic = cv2.imread('mie2016.png')
videopath = '1.flv'

def fl(gf, t):
    img = gf(t)
    temp = np.array(img)
    return cv2.bitwise_and(temp, mie_pic)

clip = VideoFileClip(videopath)
newclip = clip.fl(fl)
newclip.write_videofile('video.mp4')
