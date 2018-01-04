#!/bin/bash

#dirlist=`ls /home/research/disk1/wangshun/dataset/VOCdevkit/VOC2007/JPEGImages/*.jpg`
#dirlist=`ls test-face.txt`
dirlist=`ls yoloface-test.txt`
for temp in $dirlist
do
echo $temp
templist=`echo $temp | awk -F "/" '{print $NF}'`
fstr=`echo $templist | cut -d "." -f 1`
#echo $fstr

./darknet detector test ./cfg/face-fddb.data cfg/yolo-dog-humanface.cfg backup_dog_huamanface/yolo-dog-humanface.backup $temp -out ./testface/ 
#./darknet detector test ./cfg/combine389.data cfg/ty-yolo389.cfg backup_389/ty-yolo389.backup $temp -out ./testpng/   #>> data/test_file.txt
#./darknet detector test ./cfg/combine1_7k.data cfg/ty-kk5d2.cfg backup_1700/ty-kk5d2.backup $temp -out ./testpng/   #>> data/test_file.txt
#./darknet detector test ./cfg/combine1_7k.data cfg/yolo1700.cfg backup/yolo1700_380000.weights $temp -out ./testpng/  
#./darknet detector test ./cfg/combine389.data cfg/yolo389.cfg backup_389/yolo389.backup $temp -out ./testpng/
done



