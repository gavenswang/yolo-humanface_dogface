# coding=utf-8

# 使用说明
#将该文件放在/home/research/disk1/imagenet/ILSVRC2015/目录下

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join


def get_dirs(path):
    dirs_train = []
    dirs_2015 = os.listdir('dogs1/JPEGImages/')
    dir38 = open(path+'dog_label.txt')
    for line in dir38:
        temp = line[:-1]
        if temp in dirs_2015:
            dirs_train.append(temp)
        else:
            continue
    dir38.close()
    '''
    for dir_2015 in dirs_2015:
        dirs_train.append(dir_2015)
    '''
    
    return dirs_train


def get_classes_and_index(path):
    D = {}
    f_name = open(path+'dog_list.txt')
    
    for line in f_name:
        line_name = line.strip('\n').split(',')
        #print(line_name)
        temp_name = line_name[1]
        temp_label = line_name[0]
        D[temp_name] = temp_label
	
    f_name.close()
    return D

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


def convert_annotation(image_dir):
    #print(image_dir)
    objdir = os.listdir('dogs1/JPEGImages/'+image_dir)
    #print(objdir)
    obj_num = 0
    image_file =[]
    for idir in objdir:
        #print(idir[-4:])
        if idir[-4:] == "JPEG":
            image_file.append(idir)
    #print(image_file)
    for image in image_file:
        #print(image)
        obj_num+=1
        if obj_num == 1:
            if not os.path.exists('dogs1/labels/%s' %(image_dir)):
                os.makedirs('dogs1/labels/%s' %(image_dir))
            
        out_file = open('dogs1/labels/%s/%s.txt' % (image_dir,image.split('.')[0]),'w')
        cls_id = classes[image_dir]
        
        image_id = image.split('.')[0]
        xmlfile = 'dogs1/JPEGImages/%s/%s.xml' % (image_dir, image_id)

        if not os.path.exists(xmlfile):
            continue

        else:
             list_file.write('%s/dogs1/JPEGImages/%s/%s\n' % (wd, image_dir, image))
	     in_file = open(xmlfile)
		    
	     tree = ET.parse(in_file)
	     root = tree.getroot()
	     size = root.find('size')
	     w = int(size.find('width').text)
	     h = int(size.find('height').text)
             l =[]
	     for obj in root.iter('object'):
                 #print(obj)
		 #cls = obj.find('name').text
                 #l.append(cls)

		
		 obj_num = obj_num + 1
		 cls_id = classes[image_dir]
	         #print(cls_id)
		 xmlbox = obj.find('bndbox')
		 b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
			    float(xmlbox.find('ymax').text))
                 if w !=0 and h !=0:
		     bb = convert((w, h), b)
                 else:continue
		 '''
		 if int(cls_id) != 0:
			#print(cls_id)
                 '''
		 out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

		 '''	    
		 #list_file.write('%s/dogs1/JPEGImages/%s/%s.JPEG\n' % (wd, image_dir, image_id))
		 else:
		        continue
                 '''
             #print(l)

classes = get_classes_and_index('/home/research/disk2/wangshun/yolo1700/darknet/data/') #存放dog_list.txt文件夹的路径
print(classes)
dirs = get_dirs('/home/research/disk2/wangshun/yolo1700/darknet/data/')

wd = getcwd()

if not os.path.exists('filelist/'):
    os.mkdir('filelist')
list_file = open('filelist/%s.txt' % ('cat_label'),'w')


for image_dir in dirs:
    #print(image_dir)
    if not os.path.exists('dogs1/JPEGImages/' + image_dir):
        print("dogs1/JPEGImages/%s dir not exist" % image_dir)
        continue
    else:      
         convert_annotation(image_dir)
list_file.close()
