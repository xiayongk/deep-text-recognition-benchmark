import os

sub_dirs = ['train', 'valid', 'test']
data_path = '2nd_data'

for sub_dir in sub_dirs:
    path = os.path.join(data_path, sub_dir)
    gt_name = sub_dir + '_gt.txt'
    gt_path = os.path.join(data_path, gt_name)
    f = open(gt_path, mode='w', encoding='utf-8-sig')
    for dirpath, dirs, files in os.walk(path):
        for filename in files:
            img_path = filename
            label = filename.split('_')[0]
            row = img_path + '\t' +label + '\n' 
            f.write(row)
                
    f.close()

print('done!')
