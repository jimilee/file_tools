# -*- coding: utf-8 -*-
import os
import cv2
from tqdm import tqdm
wf_path = 'wider_face_train_bbx_gt.txt'
img_path = 'E:/face/WIDER_train/images/'
def convert_wftxt_2_txt():
    fr = open(wf_path, mode='r', encoding='utf-8')
    print(wf_path)
    with tqdm(total=185184) as pbar:
        while True:
            line = fr.readline()
            if '--' in line:
                file = img_path + line[:-1]
                src = cv2.imread(file, cv2.IMREAD_COLOR)
                iw, ih, ic = src.shape
                fw = open(file[0:-5] + '.txt', 'a', encoding='utf-8')
                bboxs = int(fr.readline())
                while bboxs > 0:
                    x1, y1, w, h, blur, exp, illum, inv, occ, pose, s = fr.readline().split(' ')
                    x1, y1, w, h = int(x1), int(y1),int(w),int(h)
                    if w < 20 or h < 20  or occ != '0': # or pose != '0' inv == '1' or blur != '0'  or
                        bboxs -= 1
                        continue
                    cx = float((x1 + (w/2))/iw)
                    cy = float((y1 + (h/2))/ih)
                    fw.write(' '.join(['10', str(cx), str(cy), str(w/iw), str(h/ih)]))
                    # print(' '.join(['10', str(cx), str(cy), str(w/iw), str(h/ih)]))
                    src = cv2.rectangle(src, (x1, y1), (x1+w, y1+h), (0,255,0),3)
                    bboxs -= 1
                # cv2.imshow("test", src)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                fw.close()
            pbar.update(1)
    fr.close()
convert_wftxt_2_txt()
