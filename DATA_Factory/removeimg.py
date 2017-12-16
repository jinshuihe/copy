#coding:utf-8
import os

'''
该程序为当标注结束后,删除未标注的图片
'''
def lll(dirl):
    zhongjian = []
    labelfilelist = os.listdir(dirl)
    for labelfile in labelfilelist:
        labelfile = labelfile.split('.')[0]
        # print(labelfile)
        labelfilelist = zhongjian.append(labelfile)
        # print(zhongjian)
    return zhongjian

def kkk():
    labelfilelist = lll(label_path)
    delPngFloder = del_img_path #删除该文件夹内的未标注图片
    imgfilelist = os.listdir(delPngFloder)
    for imgfile in imgfilelist:
        imgfile = imgfile.split('.')[0]
        if imgfile in labelfilelist:
            pass
        else:
            #print(imgfile)
            delpngPath = delPngFloder + '/' + str(imgfile) + '.png'#删除未标注png
            #delpngPath = delPngFloder + '/' + str(imgfile) + '.txt'#删除多余的txt
            try:
                os.remove(delpngPath)
            except:
                print ('error')
            print (delpngPath)


mainpath = './'
label_path = mainpath + 'label-2619'          
#待删除png或label的路径    
del_img_path = mainpath + 'image_2'

kkk()
print ('delete ok...')
