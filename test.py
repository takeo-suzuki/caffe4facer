# -*- coding: utf-8 -*-

import cv2

#HAAR分類器の顔検出用の特徴量
#cascade_path = "/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
cascade_path = "/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
#cascade_path = "/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml"
#cascade_path = "/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt_tree.xml"


image_path = "lena.jpg"

color = (255, 255, 255) #白
#color = (0, 0, 0) #黒

#ファイル読み込み
image = cv2.imread(image_path)
#グレースケール変換
image_gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)

#カスケード分類器の特徴量を取得する
cascade = cv2.CascadeClassifier(cascade_path)

#物体認識（顔認識）の実行
#image – CV_8U 型の行列．ここに格納されている画像中から物体が検出されます
#objects – 矩形を要素とするベクトル．それぞれの矩形は，検出した物体を含みます
#scaleFactor – 各画像スケールにおける縮小量を表します
#minNeighbors – 物体候補となる矩形は，最低でもこの数だけの近傍矩形を含む必要があります
#flags – このパラメータは，新しいカスケードでは利用されません．古いカスケードに対しては，cvHaarDetectObjects 関数の場合と同じ意味を持ちます
#minSize – 物体が取り得る最小サイズ．これよりも小さい物体は無視されます
#facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

print "face rectangle"
print facerect

if len(facerect) > 0:
    #検出した顔を囲む矩形の作成
    for rect in facerect:
        #cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
        x = rect[0]
        y = rect[1]
        w = rect[2]
        h = rect[3]
        image = image[rect]
        cv2.SaveImage("trim.jpg",image)
    #認識結果の保存
    #cv2.imwrite("detected.jpg", image)
