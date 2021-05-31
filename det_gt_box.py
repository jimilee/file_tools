import torch
import os
# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5x')

# Image
# img = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'
path = 'E:/Yolo_mark-master/x64/Release/data/'
# Inference
for folder_name in os.listdir(path):
    if os.path.isdir(path + folder_name + '/'):
        print(folder_name)
        # tag = ''.join([i for i in folder_name if not i.isdigit()]) + '/'
        tag = folder_name[0:2] + '/'
        for img_file in os.listdir(path + folder_name + '/'):
            fw = open(path + folder_name + '/'+img_file[0:-4]+'.txt', 'a', encoding='utf-8')
            # 파일 확장자가 (properties)인 것만 처리
            if img_file.endswith("jpg"):
                results = model(path + folder_name + '/' + img_file)
                print(results.names)
                print(results.imgs)
                for pred_data in results.pred[0].tolist():
                    x1,y1,x2,y2, conf, cls = pred_data

                    if cls == 0 :
                        # fw.write(x1/ + '\n')
                        print( x1,y1,x2,y2, conf, cls)
                # results.show()  # or .show(), .save()


