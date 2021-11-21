import os
from itertools import chain
import numpy as np
import cv2
from tqdm import tqdm

IMG_EXTENSIONS = [
    'jpg', 'jpeg',
    'png', 'bmp'
]

IMAGE_SIZE = 256
isImage = lambda x: x.split('.')[-1].lower() in IMG_EXTENSIONS
# isimg = lambda f: f.split(".")[-1].lower() in ["png", "jpg", "jpeg"]
listdir = lambda x: [os.path.join(x, f).replace('\\', '/') for f in os.listdir(x)]


def resizeImage(root: str, dest: str, resize=256):
    if not os.path.isdir(root):
        raise Exception("please provide folder of Image")
    if not os.path.isdir(dest):
        os.makedirs(dest)

    images_list = filter(isImage, listdir(root))
    images_list = sorted(list(images_list))

    pbar = tqdm(images_list)
    for img in pbar:
        name = os.path.basename(img)
        path = os.path.join(dest, name).replace('\\', '/')
        # i = cv2.imread(img, flags=cv2.IMREAD_COLOR) # not fit for chinese path
        i = cv2.imdecode(np.fromfile(img, dtype=np.uint8), -1)
        i = cv2.resize(i, dsize=(resize, resize), interpolation=cv2.INTER_AREA)
        cv2.imwrite(path, i)

def resizeCropImage(root: str, dest: str, resize=256):
    if not os.path.isdir(root):
        raise Exception("please provide folder of Image")
    if not os.path.isdir(dest):
        os.makedirs(dest)

    images_list = filter(isImage, listdir(root))
    images_list = sorted(list(images_list))

    pbar = tqdm(images_list)
    for img in pbar:
        name = os.path.basename(img)
        path = os.path.join(dest, name).replace('\\', '/')
        # i = cv2.imread(img, flags=cv2.IMREAD_COLOR) # not fit for chinese path
        i = cv2.imdecode(np.fromfile(img, dtype=np.uint8), -1)
        i = cv2.crop(i, dsize=(resize, resize), interpolation=cv2.INTER_AREA)
        cv2.imwrite(path, i)


def HsplitHalf(root: str, dest: str):
    if not os.path.isdir(root):
        raise Exception("please provide folder of Image")
    img_path = os.path.join(dest, 'image').replace('\\', '/')
    sketch_path = os.path.join(dest, 'sketch').replace('\\', '/')
    if not os.path.isdir(img_path):
        os.makedirs(img_path)
    if not os.path.isdir(sketch_path):
        os.makedirs(sketch_path)

    images_list = filter(isImage, listdir(root))
    images_list = sorted(list(images_list))
    pbar = tqdm(images_list)
    for img in pbar:
        name = os.path.basename(img)
        i_path = os.path.join(img_path, name).replace('\\', '/')
        s_path = os.path.join(sketch_path, name).replace('\\', '/')
        i = cv2.imdecode(np.fromfile(img, dtype=np.uint8), cv2.IMREAD_COLOR)
        H, W = i.shape[0], i.shape[1]
        colored = i[0:H, 0:W // 2]
        sketch = i[0:H, W // 2:W]
        # i_path = np.fromfile(i_path,dtype='uint8')
        # s_path = np.fromfile(s_path, dtype='uint8')
        cv2.imencode(".png", colored)[cv2.IMREAD_COLOR].tofile(i_path)
        cv2.imencode(".png", sketch)[cv2.IMREAD_COLOR].tofile(s_path)
        # cv2.imwrite(i_path, colored)
        # cv2.imwrite(s_path, sketch)



if __name__ == '__main__':
    # root = 'C:\\Users\\zhw\\Desktop\\数据\\anime-sketch-colorization-pair\\data\\val'
    # dest = 'C:\\Users\\zhw\\Desktop\\数据\\anime-sketch-colorization-pair-resize\\data\\val'
    # HsplitHalf(root, dest)
    root = r'C:\Users\zhw\PycharmProjects\EvaulationTool_ImageQualityMetric\dataset\real\dog_val'
    dest = r'C:\Users\zhw\PycharmProjects\EvaulationTool_ImageQualityMetric\dataset\real\dog_resize'
    resizeImage(root, dest)
