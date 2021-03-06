from read_data import read_name_list,read_file
from train_model import Model
import cv2
'''
本模块实现传输图片进行人脸识别（只在后端）
author:许如昕
create date:2020-8-5
update date:2020-8-11
'''
def test_onePicture(path):
    model= Model()
    model.load()
    img = cv2.imread(path)
    img = cv2.resize(img, (128,128))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    picType,prob = model.predict(img)
    if picType != -1:
        name_list = read_name_list(r'E:\cut-face')
        print (name_list[picType],prob)
    else:
        print ("Don't know this person")

#读取文件夹下子文件夹中所有图片进行识别
def test_onBatch(path):
    model= Model()
    model.load()
    index = 0
    img_list, label_lsit, counter = read_file(path)
    for img in img_list:
        picType,prob = model.predict(img)
        if picType != -1:
            index += 1
            name_list = read_name_list(r'E:\cut-face')
            print (name_list[picType])
        else:
            print ("Don't know this person")

    return index

if __name__ == '__main__':
    test_onePicture(r'E:\face\3.jpg')



