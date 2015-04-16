#!/bin/bash
# 諸々 build に必要なライブラリをインストールする
#sudo apt-get install build-essential
# git をインストールする
#sudo apt-get install git

# 最初に環境を最新にする
#sudo apt-get update
#sudo apt-get upgrade

# OpenCV に必須ライブラリ
sudo apt-get install cmake libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev

# OpenCV にオプションのライブラリ
sudo apt-get install libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff4-dev libjasper-dev libdc1394-22-dev

# and Other
sudo apt-get install yasm libopenexr-dev libeigen3-dev libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev libqt4-dev libqt4-opengl-dev libv4l-dev libvtk5-qt4-dev

# and etc
sudo apt-get install sphinx-common
sudo apt-get install texlive-latex-extra

# Java install
sudo apt-get install default-jdk ant

# Python install
sudo apt-get install python-dev python-pip python-numpy python-tk

# OpenCV download
wget http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.10/opencv-2.4.10.zip
unzip opencv-2.4.10.zip

# OpenCV make and install
cd opencv-2.4.10
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D WITH_VTK=ON -D WITH_CUDA=ON ..
make
sudo make install
