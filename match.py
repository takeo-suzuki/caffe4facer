#!/usr/bin/python
# coding: UTF-8

import sys, cv2, faceTools, caffe

argvs = sys.argv  # コマンドライン引数を格納したリストの取得
argc = len(argvs) # 引数の個数

if ( argc > 1 ):
    net = caffe.Classifier('deploy.prototxt','fr_train_iter_100.caffemodel', image_dims = (256, 256))
    #net.set_phase_test()# test phaseで定義されたcaffe netを使用する
    #net.set_raw_scale('data', 255)  # data layerに入力として与えられる画像の輝度上限を指定
    scores = net.predict([caffe.io.load_image(argvs[1], color = False, )], oversample=False)
    print scores