#!/bin/bash
~/caffe/build/tools/convert_imageset ./train_dataset/ ./train_dataset/train_files.txt ./train_lmdb 1 256 256
~/caffe/build/tools/convert_imageset ./test_dataset/ ./test_dataset/test_files.txt ./test_lmdb 1 256 256
