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
    fileNameNoExt = fileName.split('.')[0]
    fileNameExt = '.' + fileName.split('.')[1]
    print fileName
    print fileTag
    print fileNameNoExt
    print fileNameExt

    #imageFiles = [fileNameNoExt]
    imageFiles = []
    # trinmming face
    fileName_f = fileNameNoExt + '_f'
    image_f = faceTools.face_detect(fileName)
    cv2.imwrite(fileName_f + fileNameExt,image_f)
    
    fileName_s = fileName_f + 's'
    image_s = faceTools.resize(fileName_f + fileNameExt)
    cv2.imwrite(fileName_s + fileNameExt,image_s)
    
    imageFiles.append(fileName_s)
    
    # histgram equalize
    for fn in list(imageFiles):
        fileName_e = fn + 'e'
        image_e = faceTools.equalize(fn + fileNameExt)
        cv2.imwrite(fileName_e + fileNameExt,image_e)
        imageFiles.append(fileName_e)
    
    # reverseLR
    for fn in list(imageFiles):
        fileName_r = fn + 'r'
        image_r = faceTools.reverseLR(fn + fileNameExt)
        cv2.imwrite(fileName_r + fileNameExt,image_r)
        imageFiles.append(fileName_r)
    
    # resizeHalf
    #resizeList = []
    #for fn in list(imageFiles):
    #    fileName_s = fn + '_s'
    #    image_s = faceTools.resizeHalf(fn + fileNameExt)
    #    cv2.imwrite(fileName_s + fileNameExt,image_s)
    #    resizeList.append(fileName_s)
    #
    # resizeQuarter
    #for fn in list(imageFiles):
    #    fileName_ss = fn + '_ss'
    #    image_ss = faceTools.resizeQuarter(fn + fileNameExt)
    #    cv2.imwrite(fileName_ss + fileNameExt,image_ss)
    #    resizeList.append(fileName_ss)
    #
    # resizeEighth
    #for fn in list(imageFiles):
    #    fileName_xs = fn + '_xs'
    #    image_xs = faceTools.resizeEighth(fn + fileNameExt)
    #    cv2.imwrite(fileName_xs + fileNameExt,image_xs)
    #    resizeList.append(fileName_xs)
    #
    #imageFiles.extend(resizeList)
    
    # gray scale
    for fn in list(imageFiles):
        fileName_g = fn + 'g'
        image_g = faceTools.gray(fn + fileNameExt)
        cv2.imwrite(fileName_g + fileNameExt,image_g)
        imageFiles.append(fileName_g)
    
    # blurS
    blurList = []
    for fn in list(imageFiles):
        fileName_bs = fn + 'b'
        image_bs = faceTools.blurS(fn + fileNameExt)
        cv2.imwrite(fileName_bs + fileNameExt,image_bs)
        blurList.append(fileName_bs)

    # blurM
    for fn in list(imageFiles):
        fileName_bm = fn + 'm'
        image_bm = faceTools.blurM(fn + fileNameExt)
        cv2.imwrite(fileName_bm + fileNameExt,image_bm)
        blurList.append(fileName_bm)

    # blurL
    for fn in list(imageFiles):
        fileName_bl = fn + 'l'
        image_bl = faceTools.blurL(fn + fileNameExt)
        cv2.imwrite(fileName_bl + fileNameExt,image_bl)
        blurList.append(fileName_bl)

    imageFiles.extend(blurList)

    wf = open('train_files.txt','a')
    for fn in list(imageFiles):
        wf.write(fn + fileNameExt + ' ' + fileTag + '\n')
