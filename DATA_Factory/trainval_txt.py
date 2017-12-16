# -- coding: utf-8 --
# 生成trainval.txt文件
import os  

def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.txt':  
                # L.append(os.path.join(root, file))  
                file_name = file[0:-4]  #去掉.txt
                L.append(file_name)  
            if os.path.splitext(file)[1] == '.png':  
                # L.append(os.path.join(root, file))  
                file_name = file[0:-4]  #去掉.txt
                L.append(file_name)  
    return L  
             

mainpath = './'
label_folder = mainpath + 'label'
trainval_file = mainpath + 'ImageSets/trainval.txt'


txt_name = file_name(label_folder)

with open(trainval_file, 'w') as f:
  for i in txt_name:
    f.write('{}\n'.format(i))
f.close()

print ('trainval.txt is saved to ' + trainval_file)





