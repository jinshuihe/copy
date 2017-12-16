# -- coding: utf-8 --
'''

" "转换成","
label转换工具，四边形的４个顶点转换成最小外接矩形的４个顶点
build: lwj@20171205

'''

import os
import cv2    
import numpy as np 
from matplotlib import pyplot as plt

def load_kitti_annotation(label_path,image_name):#每一个label的坐标
    box = []
    filename = os.path.join(label_path, image_name+'.txt')
    with open(filename, 'r') as f:
        lines = f.readlines()#读取所有行
    f.close()
    for line in lines:#读取每一行
        obj = line.strip().split(' ')
        cls = obj[8]
        x0 = int(obj[0])
        y0 = int(obj[1])
        x1 = int(obj[2])
        y1 = int(obj[3])
        x2 = int(obj[4])
        y2 = int(obj[5])
        x3 = int(obj[6])
        y3 = int(obj[7])

        box.append([x0,y0,x1,y1,x2,y2,x3,y3,cls])
    return box

#获取文件名列表
def get_file_name_list(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.txt':  
                file = file[0:-4]  #去掉.txt
                L.append(file)  
    return L 


# 图像尺寸 (841,1023)
img_width = 841
img_height = 1023
label_folder = './label-2619/'  
label_new_folder = './label-rec-2619/'   
txt_name = get_file_name_list(label_folder)
img = np.zeros((img_height,img_width),np.uint8) #生成一个空灰度图像
img_copy = img.copy()    

num_exceed_bound = 0

four_points_list = []
for index in txt_name:
    four_points_list = load_kitti_annotation(label_folder,index)#标注

    label_list = []
    for pts in four_points_list:       
        # cv2.line(img,(pts[0],pts[1]),(pts[2],pts[3]),127,1)
        # cv2.line(img,(pts[2],pts[3]),(pts[4],pts[5]),255,1)
        # cv2.line(img,(pts[4],pts[5]),(pts[6],pts[7]),255,1)
        # cv2.line(img,(pts[0],pts[1]),(pts[6],pts[7]),255,1)

        #求最小外界矩形
        cnt = np.array([[pts[0],pts[1]],[pts[2],pts[3]],[pts[4],pts[5]],[pts[6],pts[7]]]) # 必须是array数组的形式
        rect = cv2.minAreaRect(cnt) # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
        # box = cv2.cv.BoxPoints(rect) # OpenCV 2. 获取最小外接矩形的4个顶点
        box = cv2.boxPoints(rect)  # OpenCV 3.x 获取最小外接矩形的4个顶点
        # cv2.line(img,(box[0][0],box[0][1]),(box[1][0],box[1][1]),127,1)
        # cv2.line(img,(box[1][0],box[1][1]),(box[2][0],box[2][1]),127,1)
        # cv2.line(img,(box[2][0],box[2][1]),(box[3][0],box[3][1]),127,1)
        # cv2.line(img,(box[3][0],box[3][1]),(box[0][0],box[0][1]),127,1)

        orient_rec_labels = str(int(box[0][0])) + ',' + str(int(box[0][1])) + ',' + \
                            str(int(box[1][0])) + ',' + str(int(box[1][1])) + ',' + \
                            str(int(box[2][0])) + ',' + str(int(box[2][1])) + ',' + \
                            str(int(box[3][0])) + ',' + str(int(box[3][1])) + ',' + \
                            str(pts[8])

        #判断矩形框是否超出图像范围(靠近边缘也删除)
        i = 0
        flag_append = True
        for i in range(0,4):
            x = box[i][0]
            y = box[i][1]
            # print (x,y)
            if int(box[i][0]) >= (img_width-2):
                flag_append = False
                print ('超出范围！')
                print (x,y)
            elif int(box[i][1]) >= (img_height-2):
                flag_append = False
                print ('超出范围！')
                print (x,y)
            elif int(box[i][0]) <= (2):
                flag_append = False
                print ('超出范围！')
                print (x,y)
            elif int(box[i][1]) <= (2):
                flag_append = False
                print ('超出范围！')
                print (x,y)


        if flag_append == True:
            label_list.append(orient_rec_labels)
            #写入新的txt文件
            new_txt_path = os.path.join(label_new_folder, index +'.txt')
            with open(new_txt_path, 'w') as f:
                for label in label_list:
                    f.write('{}\n'.format(label))
                    print (new_txt_path)
            f.close()
            cv2.line(img,(box[0][0],box[0][1]),(box[1][0],box[1][1]),127,1)
            cv2.line(img,(box[1][0],box[1][1]),(box[2][0],box[2][1]),127,1)
            cv2.line(img,(box[2][0],box[2][1]),(box[3][0],box[3][1]),127,1)
            cv2.line(img,(box[3][0],box[3][1]),(box[0][0],box[0][1]),127,1)

        else:
            num_exceed_bound = num_exceed_bound + 1
        #     cv2.line(img,(box[0][0],box[0][1]),(box[1][0],box[1][1]),127,1)
        #     cv2.line(img,(box[1][0],box[1][1]),(box[2][0],box[2][1]),127,1)
        #     cv2.line(img,(box[2][0],box[2][1]),(box[3][0],box[3][1]),127,1)
        #     cv2.line(img,(box[3][0],box[3][1]),(box[0][0],box[0][1]),127,1)

    cv2.imshow("img", img)   
    cv2.waitKey(1) 


print ('num_exceed_bound:' + str(num_exceed_bound))
print ('OK...')
cv2.waitKey(0) 
