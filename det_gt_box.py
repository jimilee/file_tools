import torch
import os
from tqdm import tqdm

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5x')

# Image Path
path = 'E:/Yolo_mark-master/x64/Release/data/'

# Inference
for folder_name in os.listdir(path):
    if os.path.isdir(path + folder_name + '/'):
        print('\n'+folder_name)
        # tag = ''.join([i for i in folder_name if not i.isdigit()]) + '/'
        tag = folder_name[0:2] + '/'
        for img_file in tqdm(os.listdir(path + folder_name + '/')):
            fw = open(path + folder_name + '/'+img_file[0:-4]+'.txt', 'a', encoding='utf-8')
            print(path + folder_name + '/'+img_file[0:-4]+'.txt')

            # 파일 확장자가 (properties)인 것만 처리
            if img_file.endswith("jpg"):
                results = model(path + folder_name + '/' + img_file)
                for pred_data in results.xywhn[0].tolist():
                    x1,y1,w,h, conf, cls = pred_data
                    if cls == 0: #person
                        fw.write('{0} {1} {2} {3} {4}\n'.format(0, x1, y1, w, h))
                    elif cls == 15: #cat
                        fw.write('{0} {1} {2} {3} {4}\n'.format(2, x1, y1, w, h))
                    elif cls == 16: #dog
                        fw.write('{0} {1} {2} {3} {4}\n'.format(3, x1, y1, w, h))
                    elif cls == 57: #sofa
                        fw.write('{0} {1} {2} {3} {4}\n'.format(4, x1, y1, w, h))
                    elif cls == 56: #chair
                        fw.write('{0} {1} {2} {3} {4}\n'.format(5, x1, y1, w, h))
                    elif cls == 72: #refreg
                        fw.write('{0} {1} {2} {3} {4}\n'.format(6, x1, y1, w, h))
                    elif cls == 62: #tv
                        fw.write('{0} {1} {2} {3} {4}\n'.format(7, x1, y1, w, h))
                    elif cls == 60: #table
                        fw.write('{0} {1} {2} {3} {4}\n'.format(8, x1, y1, w, h))
                    elif cls == 67: #phone
                        fw.write('{0} {1} {2} {3} {4}\n'.format(9, x1, y1, w, h))
                    # elif cls == 15: #face
                    #     fw.write('{0} {1} {2} {3} {4}\n'.format(2, x1, y1, w, h))
                    
                # results.show()  # or .show(), .save()
            fw.close()

