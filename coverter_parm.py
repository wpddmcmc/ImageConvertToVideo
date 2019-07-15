# -*- coding: utf-8 -*-
import cv2
import os
import argparse
import logging

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--input', type=str, default = None)
args = parser.parse_args()

if(args.input == None):
    print("Error: No input Files")
    print("Usage: To use $python3 coverter_parm.py --input data/ [--input folder saved image files]")
    exit(1)

file_path = args.input
filenames = os.listdir(file_path)
filenames.sort(key=lambda x:int(x[:-4]))

writer = cv2.VideoWriter('test_video.avi',cv2.VideoWriter_fourcc(*'MJPG'),len(filenames)/8,(1392,512),True)
for files in filenames:
    frame = cv2.imread(file_path+files)
    writer.write(frame)
writer.release()
exit(0)