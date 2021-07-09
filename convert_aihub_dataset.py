import json
import os
from tqdm import tqdm

json_path = "E:/AI_hub/반려동물 구분을 위한 동물 영상/Training/라벨링데이터_8/"
src_path = "E:/AI_hub/반려동물 구분을 위한 동물 영상/Training/원천데이터_8/"

finding_label = {"DOG": 3, "CAT": 2}

def convert_json_2_txt():
    for json_file in tqdm(os.listdir(json_path)):
        with open(json_path+json_file, 'r', encoding='utf8') as f:
            contents = f.read()
            data = json.loads(contents)
        img_path = src_path + json_file[:-4]
        img_width = data["metadata"]["width"]
        img_height = data["metadata"]["height"]
        annotations = data["annotations"]
        label = data["metadata"]["species"]
        for ano in annotations:
            filename = img_path + "/frame_{0}_timestamp_{1}.txt".format(ano["frame_number"], ano["timestamp"])
            if os.path.exists(filename): os.remove(filename)  # 이미 파일 존재시 삭제.
            fw = open(filename, 'a', encoding='utf-8')
            bbox = ano["bounding_box"]

            # object label.
            fw.write('{0} {1} {2} {3} {4}\n'.format(finding_label[str(label)],
                                                    float((bbox['x'] + ((bbox['width']) / 2)) / img_width),
                                                    float((bbox['y'] + ((bbox['height']) / 2)) / img_height),
                                                    float((bbox['width']) / img_width),
                                                    float((bbox['height']) / img_height)))
            fw.close()


convert_json_2_txt()