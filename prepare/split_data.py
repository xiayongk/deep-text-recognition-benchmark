import os
import cv2
import numpy as np

sub_dirs = ['train', 'valid', 'test']
image_path = 'D:/datasets/aihub_ocr/after/sentence'
output_path = 'D:/datasets/aihub_ocr/after/split'
label_list = set()

for sub_dir in sub_dirs:
    os.makedirs(os.path.join(output_path, sub_dir), exist_ok=True)
for dirpath, dirs, files in os.walk(image_path):
    for filename in files:
        label = filename.split('_')[0]
        label_list.add(label)

    print('label cnt: {}'.format(len(label_list)))

    for label in label_list:
        label_cnt = 0
        for filename in files:
            if label in filename:
                if label_cnt < 12:
                    input_path = os.path.join(image_path, filename)
                    ff = np.fromfile(input_path, np.uint8)
                    img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
                    save_path = os.path.join(output_path, sub_dirs[0])
                    filename = '{}_{}.jpg'.format(label, label_cnt)
                    save_path = os.path.join(save_path, filename)
                    is_success, im_buf_arr = cv2.imencode('.jpg', img)
                    im_buf_arr.tofile(save_path)
                elif label_cnt < 16:
                    input_path = os.path.join(image_path, filename)
                    ff = np.fromfile(input_path, np.uint8)
                    img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
                    save_path = os.path.join(output_path, sub_dirs[1])
                    filename = '{}_{}.jpg'.format(label, label_cnt)
                    save_path = os.path.join(save_path, filename)
                    is_success, im_buf_arr = cv2.imencode('.jpg', img)
                    im_buf_arr.tofile(save_path)
                elif label_cnt < 20:
                    input_path = os.path.join(image_path, filename)
                    ff = np.fromfile(input_path, np.uint8)
                    img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
                    save_path = os.path.join(output_path, sub_dirs[2])
                    filename = '{}_{}.jpg'.format(label, label_cnt)
                    save_path = os.path.join(save_path, filename)
                    is_success, im_buf_arr = cv2.imencode('.jpg', img)
                    im_buf_arr.tofile(save_path)
                else:
                    break
                label_cnt += 1
            





