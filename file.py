#!/usr/bin/python
# coding: UTF-8

import cv2, faceTools

f = open('files.txt')
lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines: リスト。要素は1行の文字列データ

for line in lines:
    words = line.split()
    fileName = words[0]
    fileNameNoExt = fileName.split(".")[0]
    fileNameExt = fileName.split(".")[1]
    fileTag = words[1]
    print fileName
    print fileNameNoExt
    print fileNameExt
    print fileTag
    
    image = faceTools.face_detect(fileName)
    cv2.imwrite(fileNameNoExt + "_f." + fileNameExt,image)