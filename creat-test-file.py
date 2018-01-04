import os 
from os import listdir

currentPath=os.getcwd()
listPath=currentPath+'/testpng/'
fileList=os.listdir(listPath)
out=open('yoloface-test.txt','w')
for li in fileList:
    temp=li.split('.')
    if temp[-1] in ['jpg','png','JPEG']:
        out.write(listPath+li+'\n')
out.close()
