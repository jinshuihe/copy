# -- coding: utf-8 --
'''

png2jpg
build: lwj@20171205

'''


import os
import cv2  
import numpy as np  
  

#获取文件名列表
def get_file_name_list(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.png':  
                file = file[0:-4]  #去掉 .格式
                L.append(file)  
    return L 


file_folder     = './image_2/'  
file_new_folder = './jpg-2619/'  
file_name_list = get_file_name_list(file_folder)

for file_name in file_name_list:
    file_path     = os.path.join(file_folder, file_name +'.png')
    file_new_path = os.path.join(file_new_folder, file_name +'.jpg')

    img = cv2.imread(file_path) 
    cv2.imwrite(file_new_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])  
    print (file_new_path)

print ('OK...')
