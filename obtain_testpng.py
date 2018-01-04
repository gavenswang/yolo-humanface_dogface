import os
import shutil
from os import listdir
import random
annPath = '/home/research/disk1/imagenet/ILSVRC2015/Data/CLS-LOC/train/'

imagedir = os.listdir(annPath)
with open('./data/3.8k.labels') as ann:
    for annline in ann:
        anntemp = annline.strip('\n')
        if anntemp in imagedir:
            
            imageList = os.listdir(annPath+anntemp)
            imagePath = annPath+anntemp+'/'
            shutil.copy((imagePath+imageList[random.randint(20,100)]),(os.getcwd()+'/data2'))
ann.close()

