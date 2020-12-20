import os
import json
import cv2
import numpy as np

image_path = 'D:/datasets/aihub_ocr/sentence'
output_path = 'D:/datasets/aihub_ocr/after/sentence'
imgH = 32

with open('D:/datasets/aihub_ocr/printed_data_info.json', 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)

image_label_dict = {}
for idx, image in enumerate(json_data['images']):
    image_label_dict[image['id']] = 0
for idx, annotation in enumerate(json_data['annotations']):
    if annotation['image_id'] in image_label_dict:
        image_label_dict[annotation['image_id']] = annotation['text']


os.makedirs(output_path, exist_ok=True)

cnt = 0
for dirpath, dirs, files in os.walk(image_path):
    for filename in files:
        img = cv2.imread(os.path.join(image_path, filename))
        img_h, img_w = img.shape[:-1]
        resize_w = int((imgH / img_h) * img_w)
        img = cv2.resize(img, (resize_w, imgH), interpolation=cv2.INTER_AREA)
        idx = filename.split('.png')[0]
        label = image_label_dict[idx]
        if label:
            if '\\' in label or '/' in label or ':' in label or '*' in label or '?' in label or '\"' in label or '<' in label or '>' in label or '|' in label:
                continue
            cnt += 1
            filename = '{}_{}.jpg'.format(label, cnt)
            path = os.path.join(output_path, filename)
            is_success, im_buf_arr = cv2.imencode('.jpg', img)
            im_buf_arr.tofile(path)

