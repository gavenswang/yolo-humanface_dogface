# coding=utf-8

# 使用说明
#将该文件放在/home/research/disk1/wangshun/dlib/data/CU_dogs_fully_labeled/目录下


import xml.etree.cElementTree as ET
import cv2
import numpy as np
import os
from os import listdir, getcwd
from os.path import join

def imageBox(tree):
    item = {}
    for elem in tree.iterfind('images/image'):
	#print(elem.tag,elem.attrib)
	image_file = elem.attrib["file"]
	box = []
	    
	for sub_elem in elem:
            #print(sub_elem.tag,sub_elem.attrib)
            top = sub_elem.attrib["top"]
            left = sub_elem.attrib["left"]
            width = sub_elem.attrib["width"]
            height = sub_elem.attrib["height"]
            xmin = float(left)
            ymin = float(top)
            xmax = xmin+float(width)
            ymax = ymin+float(height)
            box.append([xmin,xmax,ymin,ymax])
        item[image_file] = box
    return item
	    

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def getImageSize(fn):
    print ('load %s as ...' % fn)
    img = cv2.imread(fn)
    sp = img.shape
    
    h = sp[0]#height(rows) of image
    w = sp[1]#width(colums) of image
  
    return w,h


tree = ET.ElementTree(file='training.xml')
item = imageBox(tree)
wd = getcwd()

if not os.path.exists('filelist/'):
    os.mkdir('filelist')
list_file = open('filelist/%s.txt' %('doglabel'),'w')
for img in item:
    w,h = getImageSize(img)
    temp = img.split("/")
    imgPath = temp[0]+"/"+temp[1]+"/"
    imgtype = temp[-1].split(".")[-1]
    imgtxt = temp[-1].replace(imgtype,"txt")
    if not os.path.exists("labels/%s" %(temp[1])):
        os.makedirs("labels/%s" %(temp[1]))
    
    imagebox = item[img]
    bbox_numble = len(imagebox)
    if bbox_numble == 0:
        print("image"+image+"has no box")
        continue
    else:
        out_file = open("labels/%s/%s" %(temp[1],imgtxt),"w")
        list_file.write("%s/JPEGImages/%s/%s\n" %(wd,temp[1],temp[-1]))
        for nb in range(bbox_numble):
            b = imagebox[nb]
            bb = convert((w,h),b)
            out_file.write("1 "+ " ".join([str(a) for a in bb])+"\n") 
        out_file.close()
list_file.close()
      
