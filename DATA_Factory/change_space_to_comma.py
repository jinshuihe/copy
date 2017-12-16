
#将标注文字中的空格替换为逗号,保存到新的文件夹中

#coding:utf-8
import os


label_path = './label/'     
new_label_path = './label_new/'
labelfilelist = os.listdir(label_path)     

for label_name in labelfilelist:
    with open(label_path + label_name) as f:
        for (i, line) in enumerate(f):
            line = line.replace(' ',',') #空格替换为逗号
            #写入新文件中
            with open(new_label_path + label_name, 'a+') as f: # a+ 可以加入最后一行
                    f.write(line)  # 写入坐标    


print ('change ok...')
