import torch
import os
import face_recognition
from tqdm import tqdm

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5l')
# if torch.cuda.is_available():
#     model = model.cuda()

# Image Path
path = 'E:/Yolo_mark-master/x64/Release/data/img/'

# target labels.  #person   #dog    #cat     #chair    #tv     #phone
finding_label = {"0": 0,   "16": 3, "15": 2, "56": 4, "62": 5, "67" : 6}


#finding_label_fin = {'0': "person", '1' : "fire", '2': "cat", '3': "dog", '4': "chair", '5': "tv",  '6' : "phone",  '7' : "face"}
finding_label_fin = {"0": 0}
# Inference
for folder_name in os.listdir(path):
    if os.path.isdir(path + folder_name + '/'): #폴더인지 확인.
        print('\n'+folder_name)
        # tag = ''.join([i for i in folder_name if not i.isdigit()]) + '/'
        tag = folder_name[0:2] + '/'
        for img_file in tqdm(os.listdir(path + folder_name + '/')):
            if os.path.isfile(path + folder_name + '/' + img_file):  # 파일인지 확인.
                # if os.path.exists(path + folder_name + '/'+img_file[0:-4]+'.txt'): continue  # 이미 파일 존재시 패스.
                fw = open(path + folder_name + '/'+img_file[0:-4]+'.txt', 'a', encoding='utf-8')
                target_flag = False

                # 파일 확장자가 (properties)인 것만 처리
                if ".png" in img_file or ".jpg" in img_file:
                    """
                    #face recpgmotion
                    image = face_recognition.load_image_file(path + folder_name + '/' + img_file)
                    face_locations = face_recognition.face_locations(image) #(top, right, bottom, left)
                    # append face boxes

                    for face_data in face_locations:
                        top, right, bottom, left = face_locations[0]
                        cx = left + ((right-left)/2)
                        cy = top + ((bottom-top)/2)
                        if len(face_locations) > 0: #face
                            fw.write('{0} {1} {2} {3} {4}\n'.format(7,
                            float(cx/(image.shape[1])),
                            float(cy/(image.shape[0])),
                            float((right-left)/image.shape[1]),
                            float((bottom-top)/image.shape[0])))
                    """

                    # append detection boxes
                    #yolov5 detector
                    results = model(path + folder_name + '/' + img_file)

                    for pred_data in results.xywhn[0].tolist():
                        x1,y1,w,h, conf, cls = pred_data
                        cls= str(int(cls))
                        # if cls == "16" or cls == "15": #강아지 or 고양이 있을때 True
                        #     target_flag = True
                        if cls in finding_label_fin.keys():
                            fw.write('{0} {1} {2} {3} {4}\n'.format(finding_label[str(cls)], x1, y1, w, h))

                    # results.show()  # or .show(), .save()
                fw.close()
                # if not target_flag: #강아지 or 고양이 없을때 삭제
                #     os.remove(path + folder_name + '/' + img_file) # remove image file
                #     os.remove(path + folder_name + '/'+img_file[0:-4]+'.txt') # remove txt file

