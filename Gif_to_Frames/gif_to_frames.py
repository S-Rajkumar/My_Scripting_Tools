#!/usr/bin/env python3

'''
Author : udmnxpdu
Date : July 2020
'''

from PIL import Image
from PIL import GifImagePlugin
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input','-i',help="Input File",required=True)
args = parser.parse_args()
in_file = args.input

imageObject = Image.open(in_file)

print("[+] Total Frames : "+str(imageObject.n_frames))

i = 1; 
print("[+] Extracting Frames...")
for frame in range(0,imageObject.n_frames):
    filename = "frame_"+ str(i) +".png"
    imageObject.seek(frame)
    imageObject.save(filename)
    i = i + 1
print("[+] Frames Extracted Done!")
