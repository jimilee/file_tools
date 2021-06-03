import torch
import os
import face_recognition
from tqdm import tqdm

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5x')

# Image Path
path = 'E:/Yolo_mark-master/x64/Release/data/'

# target labels. #person   #dog    #cat    #chair   #table   #sofa     #tv     #refreg    #phone
finding_label = {"0": 0, "16": 3, "15": 2, "56": 5, "60": 8, "57": 4, "62": 7, "72" : 6, "67" : 9}

# Inference
for folder_name in os.listdir(path):
    if os.path.isdir(path + folder_name + '/'): #폴더인지 확인.
        print('\n'+folder_name)
        # tag = ''.join([i for i in folder_name if not i.isdigit()]) + '/'
        tag = folder_name[0:2] + '/'
        for img_file in tqdm(os.listdir(path + folder_name + '/')):
            fw = open(path + folder_name + '/'+img_file[0:-4]+'.txt', 'a', encoding='utf-8')
            # print(path + folder_name + '/'+img_file[0:-4]+'.txt')

            # 파일 확장자가 (properties)인 것만 처리
            if img_file.endswith("jpg"):
                #yolov5 detector
                results = model(path + folder_name + '/' + img_file)
                #face recpgmotion
                image = face_recognition.load_image_file(path + folder_name + '/' + img_file)
                face_locations = face_recognition.face_locations(image) #(top, right, bottom, left)
                # append face boxes
                for face_data in face_locations:
                    top, right, bottom, left = face_locations[0]
                    cx = left + ((right-left)/2)
                    cy = top + ((bottom-top)/2)
                    if len(face_locations) > 0: #face
                        fw.write('{0} {1} {2} {3} {4}\n'.format(10,
                        float(cx/(image.shape[1])),
                        float(cy/(image.shape[0])),
                        float((right-left)/image.shape[1]),
                        float((bottom-top)/image.shape[0])))
                # append detection boxes
                for pred_data in results.xywhn[0].tolist():
                    x1,y1,w,h, conf, cls = pred_data
                    if str(cls) in finding_label.keys():
                        fw.write('{0} {1} {2} {3} {4}\n'.format(finding_label[str(cls)], x1, y1, w, h))

                    
                # results.show()  # or .show(), .save()
            fw.close()

