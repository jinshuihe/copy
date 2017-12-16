# Author: Wenjun Luo
# -- coding: utf-8 --
import numpy as np
import cv2
import os

#水平镜像翻转
def data_mirror_copy(name, img_dir, out_img_dir, label_dir, out_label_dir):
    #保存镜像img
    img_path = img_dir + name + '.png'
    out_img_path = out_img_dir + name + '_mirror.png'
    try:
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)#BGR
        height = img.shape[0]
        width = img.shape[1]
        #img3=img[::-1]#垂直镜像
        img_mirror = img[:,::-1]#水平镜像
        cv2.imwrite(out_img_path, img_mirror)
    except:
        print('read img error')

    #保存镜像label
    box = []
    try:
        filename = os.path.join(label_dir, name + '.txt')
    except:
        print('%s%s.txt 读取错误'%(label_dir, name))
    with open(filename, 'r') as f:
        lines = f.readlines()#读取所有行
    f.close()

    for line in lines:#读取每一行
        obj = line.strip().split(' ')#.strip()默认删除空白符（包括'\n', '\r',  '\t',  ' ');.split(' ')按某一个字符分割
        cls = obj[0]
        xmin = int(obj[4])
        ymin = int(obj[5])
        xmax = int(obj[6])
        ymax = int(obj[7])
        # ori:   x1,y1,x2,y2
        # after: w-x2,y1,w-x1,y2
        xmin = abs(width - int(obj[6]))#??
        ymin = int(obj[5])
        xmax = abs(width - int(obj[4]))#??
        ymax = int(obj[7])
        if len(obj) >= 15:
            score = float(obj[15])
            box.append([cls,xmin,ymin,xmax,ymax,score])
        else:
            box.append([cls,xmin,ymin,xmax,ymax])

        out_label_path = out_label_dir + name + '_mirror.txt'
        str_obj = str(obj)
        with open(out_label_path, 'a+') as f:# a+ 可以加入最后一行
            str_write = str(obj[0]) + ' ' + str(obj[1]) + ' ' + str(obj[2]) + ' ' + str(obj[3])
            str_write = str_write + ' ' + str(xmin) + ' ' + str(ymin) + ' ' + str(xmax) + ' ' + str(ymax)
            f.write(str_write + '\n')
            f.close()
    # #查看镜像后的标注
    # try:
    #     img_rec = cv2.imread(out_img_path, cv2.IMREAD_COLOR)#BGR
    #     cv2.rectangle(img_rec, (xmin, ymin), (xmax, ymax), (0, 255, 0), 1)
    #     cv2.imwrite(out_img_path, img_rec) 
    # except:
    #     print('rectabgle error')

data_path = './KITTI/'
trainval_file = data_path + 'ImageSets/trainval.txt'
img_dir = data_path + 'training/image_2/'
# out_img_dir = data_path + 'training/image_mirror/'
out_img_dir = data_path + 'training/image_2/'
label_dir = data_path + 'training/label_2/'
# out_label_dir = data_path + 'training/label_mirror/'
out_label_dir = data_path + 'training/label_2/'

idx = []
with open(trainval_file) as f:
    for line in f:
        idx.append(line.strip())
f.close()

total_num = len(idx)

i = 0
for name in idx:   
    data_mirror_copy(name, img_dir, out_img_dir, label_dir, out_label_dir)
    print ('%d / %d  ok'%(i,total_num))
    i += 1






