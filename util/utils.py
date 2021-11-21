import os
from itertools import chain
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
isImage = lambda x: x.split('.')[-1].lower() in ['jpg', 'jepg', 'png', 'bmp']
listdir = lambda x: [os.path.join(x, f).replace('\\', '/') for f in os.listdir(x)]

def num2tuple(num):
    return num if isinstance(num, tuple) else (num, num)

def openImage(file):
    if not os.path.exists(file):
        raise FileExistsError('not found!')
    if not isImage(file):
        raise RuntimeError("illegal image file!")
    image = Image.open(file).convert("RGB")
    return image

def center_crop_and_resize(file,size=256):
    img = center_crop(file)
    return img.resize(num2tuple(size),resample = Image.ANTIALIAS)

def center_crop(img):
    width, height = img.size
    keep = width if width<height else height
    left = int(np.ceil((width - keep) / 2))
    right = width - int(np.floor((width - keep) / 2))
    top = int(np.ceil((height - keep) / 2))
    bottom = height - int(np.floor((height - keep) / 2))

    center_cropped_img = img.crop((left, top, right, bottom))

    return center_cropped_img


def makeDatasetList_dir(root):
    root_list = chain(*(filter(isImage, folder) for folder in listdir(root)))
    root_list = sorted(list(root_list))
    return root_list

def makeDatasetList(root):
    root_list = chain(*(filter(isImage, listdir(folder)) for folder in listdir(root)))
    root_list = sorted(list(root_list))
    return root_list