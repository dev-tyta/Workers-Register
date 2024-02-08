import os
import cv2


data_path = "../../data/player_data"


def preprocess(path):
    images = []
    names = []
    img_list = os.listdir(path)

    for img in img_list:
        img_read = cv2.imread(f"{data_path}/{img}")
        images.append(img_read)
        names.append(os.path.splitext(img)[0])

    return images, names


# testing function
# img_pre, img_name = preprocess(data_path)
#
# print(f"{img_pre}, {img_name}")
