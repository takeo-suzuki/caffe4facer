#!/usr/bin/python
# coding: UTF-8

import cv2, faceTools

f = open('files.txt')
lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines: リスト。要素は1行の文字列データ

for line in lines:
    fileName = line.split()[0]
    fileTag = line.split()[1]
    fileNameNoExt = fileName.split(".")[0] + "_"
    fileNameExt = "." + fileName.split(".")[1]
    print fileName
    print fileTag
    print fileNameNoExt
    print fileNameExt

    imageFiles = [fileNameNoExt]
    # trinmming face
    fileName_f = fileNameNoExt + "f" + fileNameExt
    image_f = faceTools.face_detect(fileName)
    cv2.imwrite(fileName_f,image_f)
    imageFiles.append(fileName_f)
    
    # histgram equalize
    for fn in list(imageFiles):
        fileName_e = fn + "e" + fileNameExt
        image_e = faceTools.equalize(fn)
        cv2.imwrite(fileName_e,image_e)
        imageFiles.append(fileName_e)
    
    # reverseLR
    for fn in list(imageFiles):
        fileName_r = fn + "r" + fileNameExt
        image_r = faceTools.reverseLR(fileName)
        cv2.imwrite(fileName_r,image_r)
        imageFiles.append(fileName_r)
