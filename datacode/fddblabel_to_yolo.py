import os,cv2
from math import *
import numpy as np
def show_annotations():
        for i in range(10):
            if i >=9:
                annotationfilepath=annotationdir+"/FDDB-fold-%d-ellipseList.txt" %(i+1)
            else:
                annotationfilepath=annotationdir+"/FDDB-fold-0%d-ellipseList.txt" %(i+1)    
            annotationfile=open(annotationfilepath)  
            while(True):  
                filename=annotationfile.readline()[:-1]+".jpg"  
                if not filename:  
                    break  
                line=annotationfile.readline()  
                if not line:  
                    break  
                print filename  
                facenum=(int)(line)  
                img=cv2.imread(origimagedir+"/"+filename)  
                #filename=filename.replace('/','_')  
                #cv2.imwrite(imagesdir+"/"+filename,img)  
                w = img.shape[1]  
                h = img.shape[0]  
                #print(w,h)
                filepathList=filename.split('/')
                filepath=''
                for i in range(len(filepathList)):
                    if i < (len(filepathList)-1):
                        filepath=filepath+'/'+filepathList[i]
                    else:
                        imgname = filepathList[i]
                    
                if not os.path.exists(labelsdir+'/'+filepath):
                    os.makedirs(labelsdir+'/'+filepath) 
                labelpath=labelsdir+filepath+'/'+imgname[:-3]+"txt"  
                fileList.write(origimagedir+filepath+'/'+imgname+'\n')
                labelfile=open(labelpath,'w')     
                for j in range(facenum):  
                    line=annotationfile.readline().strip().split()  
                    major_axis_radius=(float)(line[0])  
                    minor_axis_radius=(float)(line[1])  
                    angle=(float)(line[2])  
                    center_x=(float)(line[3])  
                    center_y=(float)(line[4])  
                    score=(float)(line[5])  
                    angle = angle / 3.1415926*180  
                    cv2.ellipse(img, ((int)(center_x), (int)(center_y)), ((int)(major_axis_radius), (int)(minor_axis_radius)), angle, 0., 360.,(255, 0, 0))   
                    
                    if convert2rects:  
                        mask=np.zeros((img.shape[0],img.shape[1]),dtype=np.uint8)  
                        cv2.ellipse(mask, ((int)(center_x), (int)(center_y)), ((int)(major_axis_radius), (int)(minor_axis_radius)), angle, 0., 360.,(255, 255, 255))  
                        #cv2.imshow("mask",mask)   
                        contours=cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)  
                    
                        for k in range(len(contours)-2):  
                            r=cv2.boundingRect(contours[k])  
                            x_min=r[0]  
                            y_min=r[1]  
                            x_max=r[0]+r[2]  
                            y_max=r[1]+r[3]  
                            xcenter=r[0]+r[2]/2  
                            ycenter=r[1]+r[3]/2  
                            labelline="0"+" "+str(xcenter*1.0/w) + ' ' + str(ycenter*1.0/h) + ' ' + str(r[2]*1.0/w) + ' ' + str(r[3]*1.0/h) + '\n'  
                            labelfile.write(labelline)  
                            #cv2.rectangle(img,(int(x_min),int(y_min)),(int(x_max),int(y_max)),(0,0,255))  
                labelfile.close()  
                #cv2.imshow("img",img)  
                #cv2.waitKey(1)  
rootdir="/home/research/disk1/wangshun/dataset/data/fddb"
origimagedir=rootdir+"/images"
#imagesdir=rootdir+"/images"
annotationdir=rootdir+"/FDDB-folds"
labelsdir=rootdir+"/labels"
#Annotationsdir=rootdir+"/Annotations"
convert2rects=True
#bsavexmlanno=True
bsavetxtanno=True
#datasetprefix="/home/yanhe/data/fddb/images/"
#labelsdir = '/home/research/disk1/wangshun/dataset/data/labels'
#annotationdir='/home/research/disk1/wangshun/dataset/data/FDDB-folds'
if not os.path.exists(rootdir+'/filelist/'):
    os.makedirs(rootdir+'/filelist/')
fileList = open(rootdir+'/filelist/fddbtrain.txt','w')
show_annotations()

