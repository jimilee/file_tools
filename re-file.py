# -*- coding: utf-8 -*-
import os
import fileinput
import sys
#각종 학습 데이터 파일들 가공을 위한 메소드들 모음집. -지미
# target labels.  #person   #dog    #cat     #chair   #table   #sofa     #tv     #refreg    #phone
from tqdm import tqdm

finding_label = {'0': "person",'1' : "fire",'2': "cat", '3': "dog", '4': "sofa",  '5': "chair", '6' : "refreg",'7': "tv",  '8': "table",  '9' : "phone",  '10' : "face"}
finding_label_fin = {'0': "person",'1' : "fire",'2': "cat", '3': "dog", '4': "chair", '5': "tv",  '6' : "phone",  '7' : "face"}
remove_label = {'4': "sofa",  '6' : "refreg",  '8': "table"}
def modify_gt_file():
    # 현재 위치(.)의 파일을 모두 가져온다.
    path = 'E:/Yolo_mark-master/x64/Release/data/img/'
    for folder in os.listdir(path):
        print(path + folder + '/')
        for filename in tqdm(os.listdir(path + folder + '/')):
            # 파일 확장자가 (properties)인 것만 처리
            if filename.endswith("txt"):
                for line in fileinput.input(path + folder + '/' + filename, inplace=True):
                    label, cx, cy, w, h = line.split(' ')
                    #if label in remove_label:
                    #    continue
                    if label == '0': #person
                        label = '0'
                        continue
                    else:
                        sys.stdout.write(' '.join([label, cx, cy, w, h]))

"""
                    #elif label == '81': #face
                    #    label = '10'
                    #    sys.stdout.write(' '.join([label, cx, cy, w, h]))
                    #elif label == '15': #cat
                        label = '2'
                        sys.stdout.write(' '.join([label, cx, cy, w, h]))
                    elif label == '16': #dog
                        label = '3'
                        sys.stdout.write(' '.join([label, cx, cy, w, h]))
"""
# def make_train_file():
#     cnt = 0
#     # 현재 위치(.)의 파일을 모두 가져온다.
#     path = "/home/ljm/darknet/obj/"
#     #path = "E:/MOT16/train/"
#     respath = "/home/ljm/darknet/obj/train.txt"
#     respath2 = "/home/ljm/darknet/obj/test.txt"
#     train_fw = open(respath, 'a')
#     test_fw = open(respath2, 'a')
#     for filename in os.listdir(path):
#         #print(path + filename +"/")
#         if filename == "MOT16-10" or filename == "MOT16-09":
#             for img_name in os.listdir(path + filename + "/"):
#                 if img_name.endswith("jpg"):
#                     print(path + filename + "/" + img_name)
#                     test_fw.write(path + filename + "/" + img_name + '\n')
#         else:
#             for img_name in os.listdir(path + filename + "/"):
#                 if img_name.endswith("jpg"):
#                     print(path + filename + "/" + img_name)
#                     train_fw.write(path + filename + "/" + img_name + '\n')
#
#     test_fw.close()
#     train_fw.close()

def check_filename():
    pre_num = 0
    # 현재 위치(.)의 파일을 모두 가져온다.
    # 'C:/Yolo_mark - master/x64/Release/data/img/'
    # path = 'C:/Yolo_mark-master/x64/Release/data/img/'
    path = 'E:/Etri/Quater/'
    # respath = "/home/ljm/darknet/obj/MOT16-02/train.list"
    # fw = open(respath, 'a', encoding='utf-8')
    for filename in os.listdir(path):
        # 파일 확장자가 (properties)인 것만 처리
        if filename.endswith("png"):
            number = filename.split('_')[0]
            if number == pre_num :
                print('occuluded. -- ', number)
            pre_num = number

# def make_list_file(): # 에트리 데이터셋
#     cnt = 0
#     # 현재 위치(.)의 파일을 모두 가져온다.
#     # 'C:/Yolo_mark - master/x64/Release/data/img/'
#     # path = 'C:/Yolo_mark-master/x64/Release/data/img/'
#     path = 'E:/Etri/Euler/'
#     respath = 'E:/Etri/Euler/list.txt'
#     fw = open(respath, 'a', encoding='utf-8')
#
#     while cnt < 276:
#         for filename in os.listdir(path):
#             # 파일 확장자가 (properties)인 것만 처리
#             if filename.endswith("png"):
#                 file_number = filename.split('_')[0]
#                 if cnt == int(file_number):
#                     fw.write(filename[0:-4] + '\n')
#                     print(file_number , cnt , 'matched')
#                     cnt+=1
#                     break
#
#     fw.close()

def count_labels():
    cnt = {}
    # 현재 위치(.)의 파일을 모두 가져온다.
    path = 'Z:/Define_dataset/IR/'
    # path = 'E:/Yolo_mark-master/x64/Release/data/test/'
    # path = 'C:/Users/USER/Desktop/Etri/Capture/10프레임_rename/'
    # respath = "/home/ljm/darknet/obj/MOT16-02/train.list"
    # fw = open(respath, 'a', encoding='utf-8')
    # total = len(os.listdir(path))
    for folder_name in os.listdir(path):
        if os.path.isdir(path + folder_name + '/'):
            print(folder_name)
            # tag = ''.join([i for i in folder_name if not i.isdigit()]) + '/'
            tag = folder_name[0:2]+'/'
            for txt_file in os.listdir(path+folder_name+'/'):
                # 파일 확장자가 (properties)인 것만 처리
                if txt_file.endswith("txt"):
                    for line in open(path + folder_name + '/' + txt_file, mode='rt',encoding='utf-8'):
                        label, cx, cy, w, h = line.split(' ')
                        if label == '81':
                            print(txt_file)
                        if not label in finding_label_fin.keys():
                            print(txt_file, label)
                            continue
                        try:
                            cnt[str(tag+finding_label_fin[str(label)])]+=1
                        except:
                            cnt.update({str(tag+finding_label_fin[str(label)]):0})
    print(cnt)
def rename_file():

    # 현재 위치(.)의 파일을 모두 가져온다.
    # path = 'E:/Yolo_mark-master/x64/Release/data/'
    # path = 'Z:/Define_dataset/'
    path = 'E:/디파인/fireData/'
    # respath = "/home/ljm/darknet/obj/MOT16-02/train.list"
    # fw = open(respath, 'a', encoding='utf-8')
    for folder in tqdm(os.listdir(path)):
        cnt = 0
        # if folder.endswith(".mp4"):
        #     folder_id = folder.split('-')[2][0:-4]
        # else:
        #     folder_id = folder.split('-')[2]
        # print(folder.split('-')[2][0:-4])
        if os.path.isdir(path+folder+'/'):
            total = len(os.listdir(path+folder+'/'))
            while cnt < total:
                for filename in os.listdir(path+folder+'/'):
                    print(filename.split('_')[1][0:-4])
                    if filename.split('_')[0] == folder:
                        cnt = total+1
                        continue
                    else:
                        new_filename = ""
                        try:
                            number = int(filename.split('_')[1][0:-4])
                            # if number == cnt:
                            # 파일명에서 AA를 BB로 변경하고 파일명 수정

                            new_filename = "{0:04}".format(number) #이름 {폴더명}_{0:08d}.jpg ##
                            # new_filename = filename

                            new_filename = folder + "_" + new_filename
                            # print(new_filename)
                            # os.rename(path+folder+'/'+filename, path+folder+'/'+new_filename)
                            os.rename(path+folder+'/'+filename, path+folder+'/'+new_filename+'.jpg')
                            cnt +=1
                        except:
                            print('에러.',path+folder+'/'+filename, '->' ,path+folder+'/'+new_filename)
                            cnt +=1
                            continue
        else: continue

def rename_filefolder():
    # 현재 위치(.)의 파일을 모두 가져온다.
    path = 'E:/디파인/fireData/Fireimages/'
    # respath = "/home/ljm/darknet/obj/MOT16-02/train.list"
    # fw = open(respath, 'a', encoding='utf-8')
    if os.path.isdir(path+'/'):
        total = len(os.listdir(path+'/'))
        cnt = 0
        while cnt < total:
            for filename in os.listdir(path+'/'):
                new_filename = ""
                try:
                    # print(filename[3:])
                    os.rename(path+'/'+filename, path+'/DT_fireimages'+"_{0:04}.jpg".format(cnt))
                    cnt +=1
                except:
                    print('에러.',path+'/'+filename, '->' ,path+'/'+new_filename)
                    cnt +=1
                    continue


if __name__ == "__main__":
    # make_train_file()
    #rename_file()
    # check_filename()
    # make_list_file()
    # modify_gt_file()
    count_labels()
    #rename_filefolder()