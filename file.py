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
    
    # trinmming face
    fileName_f = fileNameNoExt + "_f." + fileNameExt
    image_f = faceTools.face_detect(fileName)
    cv2.imwrite(fileName_f,image_f)
    
    # histgram equalize
    fileName_e = fileNameNoExt + "_e." + fileNameExt
    image_e = faceTools.equalize(fileName)
    cv2.imwrite(fileName_e,image_e)
    
    # histgram equalize
    fileName_fe = fileNameNoExt + "_fe." + fileNameExt
    image_fe = faceTools.equalize(fileName_f)
    cv2.imwrite(fileName_fe,image_fe)
    
    # reverseLR
    fileName_r = fileNameNoExt + "_r." + fileNameExt
    image_r = faceTools.reverseLR(fileName)
    cv2.imwrite(fileName_r,image_r)
