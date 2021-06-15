# -*- coding: utf-8 -*-
import os
import cv2
from tqdm import tqdm
wf_path = 'wider_face_val_bbx_gt.txt'
img_path = 'E:/face/WIDER_val/images/'
def convert_wftxt_2_txt():
    fr = open(wf_path, mode='r', encoding='utf-8')
    print(wf_path)
    with tqdm(total=159420) as pbar:
        while True:
            line = fr.readline()
            if '--' in line:
                file = img_path + line[:-1]
                src = cv2.imread(file, cv2.IMREAD_COLOR)
                ih, iw, ic = src.shape
                if os.path.exists(file[0:-4] + '.txt'):
                    os.remove(file[0:-4] + '.txt')#이미 파일존재하면, 삭제.

                fw = open(file[0:-4] + '.txt', 'a', encoding='utf-8')
                bboxs = int(fr.readline())
                while bboxs > 0:
                    x1, y1, w, h, blur, exp, illum, inv, occ, pose, s = fr.readline().split(' ')
                    x1, y1, w, h = float(x1), float(y1), float(w),float(h)
                    if w < 20 or h < 20  or occ != '0': # or pose != '0' inv == '1' or blur != '0'  or
                        bboxs -= 1
                        pbar.update(1)
                        continue
                    cx = float((x1 + (w/2))/iw)
                    cy = float((y1 + (h/2))/ih)
                    fw.write(' '.join(['10', str(cx), str(cy), str(w/iw), str(h/ih)]) + '\n')
                    pbar.update(1)
                    # src = cv2.rectangle(src, (x1, y1), (x1+w, y1+h), (0,255,0),3)
                    bboxs -= 1
                # cv2.imshow("test", src)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                fw.close()

    fr.close()
convert_wftxt_2_txt()
