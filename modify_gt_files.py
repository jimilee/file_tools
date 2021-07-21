from tqdm import tqdm
import os
import fileinput
import sys

remove_label = {'4': "sofa",  '6' : "refreg",  '8': "table"}
def modify_gt_file():
    # 현재 위치(.)의 파일을 모두 가져온다.
    path = 'E:/디파인/'
    for folder in os.listdir(path):
        print(path + folder + '/')
        for filename in tqdm(os.listdir(path + folder + '/')):
            # 파일 확장자가 (properties)인 것만 처리
            if filename.endswith("txt"):
                for line in fileinput.input(path + folder + '/' + filename, inplace=True):
                    label, cx, cy, w, h = line.split(' ')
                    if label in remove_label.keys():
                        continue
                    if label == '5': #chair
                        sys.stdout.write(' '.join(['4', cx, cy, w, h]))
                    elif label == '7': #tv
                        sys.stdout.write(' '.join(['5', cx, cy, w, h]))
                    elif label == '9': #phone
                        sys.stdout.write(' '.join(['6', cx, cy, w, h]))
                    elif label == '10': #face
                        sys.stdout.write(' '.join(['7', cx, cy, w, h]))
                    else:
                        sys.stdout.write(' '.join([label, cx, cy, w, h]))