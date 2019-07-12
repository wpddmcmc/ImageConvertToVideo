# -*- coding: utf-8 -*-
import cv2
import os
file_path = "data/"

filenames = os.listdir(file_path)
filenames.sort(key=lambda x:int(x[:-4]))

writer = cv2.VideoWriter('test_video.avi',cv2.VideoWriter_fourcc(*'MJPG'),len(filenames)/8,(1392,512),True)
for files in filenames:
    frame = cv2.imread(file_path+files)
    writer.write(frame)
writer.release()
