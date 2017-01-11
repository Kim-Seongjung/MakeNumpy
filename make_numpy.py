'''
Created on 2017. 1. 3.

@author: Seongjung
'''

import utility_
from nbconvert.filters.strings import path2url
from setuptools.sandbox import save_path


divide_ind=120
path1='C:\\Users\\Seongjung\\Desktop\\eye\\normal\\'
path2='C:\\Users\\Seongjung\\Desktop\\eye\\ab_normal\\'
train_rate=0.8 
val_rate=0.1
save_path='D:\\data\\Eye\\npy\\npy_256\\'
img_row=256
img_col=256
color_ch=3

utility_.pic2numpy_TVT_divide_modify(divide_ind, path1, path2, train_rate, val_rate, save_path, img_row, img_col, color_ch, n_data='same')