#---------------------------------------------#
#   运行前一定要修改classes
#   如果生成的2007_train.txt里面没有目标信息
#   那么就是因为classes没有设定正确
#---------------------------------------------#
import xml.etree.ElementTree as ET
from os import getcwd

sets=[('car', 'train'), ('car', 'val'), ('car', 'test')]
#-----------------------------------------------------#
#   这里设定的classes顺序要和model_data里的txt一样
#-----------------------------------------------------#
classes = ['licence']

def convert_annotation( image_id, list_file):
    in_file = open('/home/yanran/Desktop/FASTER-RCNN/VOC/Annotations/%s.xml'%(image_id), encoding='utf-8')
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = 0 
        if obj.find('difficult')!=None:
            difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(float(xmlbox.find('xmin').text)), int(float(xmlbox.find('ymin').text)), int(float(xmlbox.find('xmax').text)), int(float(xmlbox.find('ymax').text)))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for car, image_set in sets:
    image_ids = open('/home/yanran/Desktop/FASTER-RCNN/VOC/ImageSets/Main/%s.txt'%( image_set), encoding='utf-8').read().strip().split()
    list_file = open('/home/yanran/Desktop/FASTER-RCNN/%s_%s.txt'%(car, image_set), 'w', encoding='utf-8')
    for image_id in image_ids:
        list_file.write('/home/yanran/Desktop/FASTER-RCNN/VOC/JPEGImages/%s.jpg'%(image_id))
        convert_annotation( image_id, list_file)
        list_file.write('\n')
    list_file.close()
