import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree
import os
#face 디텍션을 위한 PASCAL dataset -> YOLO format 가공.
xml_path = "E:/TrainVal/VOCdevkit/VOC2011/Annotations/"
txt_path = "E:/TrainVal/VOCdevkit/VOC2011/YoloAnnotations/"


finding_label = {"person": 0, "dog": 3, "cat": 2, "chair": 5, "diningtable": 8, "sofa": 4, "tvmonitor": 7, "head":10}
def convert_xml_2_txt():
    for xml_file in os.listdir(xml_path):
        print(xml_file)
        data = ET.parse(xml_path + xml_file)
        root = data.getroot()
        fw = open(txt_path + xml_file[:-4] + '.txt', 'a', encoding='utf-8')

        #get image_size.
        img_size = root.findall("size")
        img_width = int(img_size[0].find("width").text)
        img_height = int(img_size[0].find("height").text)

        print(img_size)

        for tag in root.iter("object"):
            if tag.find("name").text in finding_label.keys():
                xmin = int(tag.find("bndbox").findtext("xmin"))
                ymin = int(tag.find("bndbox").findtext("ymin"))
                xmax = int(tag.find("bndbox").findtext("xmax"))
                ymax = int(tag.find("bndbox").findtext("ymax"))

                # object label.
                fw.write('{0} {1} {2} {3} {4}\n'.format(finding_label[tag.find("name").text],
                                                        float((xmin + ((xmax - xmin) / 2)) / img_width),
                                                        float((ymin + ((ymax - ymin) / 2)) / img_height),
                                                        float((xmax - xmin) / img_width),
                                                        float((ymax - ymin) / img_height)))

        for tag in root.iter("part"): #person's part.
            if tag.find("name").text == "head":
                xmin = int(tag.find("bndbox").findtext("xmin"))
                ymin = int(tag.find("bndbox").findtext("ymin"))
                xmax = int(tag.find("bndbox").findtext("xmax"))
                ymax = int(tag.find("bndbox").findtext("ymax"))

                #face label.
                fw.write('{0} {1} {2} {3} {4}\n'.format(10,
                                                        float((xmin + ((xmax-xmin)/2)) / img_width),
                                                        float((ymin + ((ymax-ymin)/2)) / img_height),
                                                        float((xmax - xmin) / img_width),
                                                        float((ymax - ymin) / img_height)))

        fw.close()

convert_xml_2_txt()