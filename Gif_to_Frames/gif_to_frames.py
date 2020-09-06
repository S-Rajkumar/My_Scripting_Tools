#!/usr/bin/env python3

'''
Author : udmnxpdu
Date : July 2020
'''

from PIL import Image
from PIL import GifImagePlugin
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input','-i',help="Input File",required=True)
args = parser.parse_args()
in_file = args.input
dir_name = in_file.split(".")[0]
os.system("mkdir "+dir_name)
imageObject = Image.open(in_file)

print("[+] Total Frames : "+str(imageObject.n_frames))

i = 1; 
print("[+] Extracting Frames...")
for frame in range(0,imageObject.n_frames):
    filename = dir_name+"/frame_"+ str(i) +".png"
    imageObject.seek(frame)
    imageObject.save(filename)
    i = i + 1
print("[+] Frames Extracted Done!")
