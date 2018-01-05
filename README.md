![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

*project1:

yolo进行人脸狗脸检测

人脸数据fddb+dlib

fddb：将datacode/fddblabel_to_yolo.py放在fddb数据文件夹下

     执行python ./fddblabel_to_yolo.py
     
     生成filelist1.txt
     
dlib:将datacode/facedata_to_yolo.py放在dlib数据文件夹下

     执行python ./facedata_to_yolo.py
     
     生成filelist2.txt
     
狗脸数据dogs1（Imagenet）

    将datacode/dogdata_to_yolo.py放在dogs1文件夹外
    
    执行python ./dogdata_to_yolo.py
    
    生成filelist3.txt
    
cat filelist1.txt filelist2.txt filelist3.txt > train.txt

train：

     ./darknet detector train cfg/face-fddb.data cfg/yolo-dog-humanface.cfg yolo-face.backup -gpus 0,1
     
test:

    先将要测试的图片放在testpng文件夹中
    
    执行python ./creat-test-file.py
    
    生成yoloface-test.txt
    
    ./yolotest.sh
    
#Darknet#
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).
