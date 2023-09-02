import os
import cv2

#read imdb data
def read_imdb(data_dir, is_train=True):
    data = []
    for label in ['pos', 'neg']:
        path = os.path.join(data_dir, label)
        #print(path)
        #print(os.listdir(path))
        for file in os.listdir(path):
            with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
                data.append([f.read(), 1 if label == 'pos' else 0])
    return data

#read cv2 image
def read_cv2_image(image_dir):
    data = []
    for label in ['pos', 'neg']:
        path = os.path.join(image_dir, label)
        #print(path)
        #print(os.listdir(path))
        for file in os.listdir(path):
            data.append([cv2.imread(os.path.join(path, file)), 1 if label == 'pos' else 0])
    return data
