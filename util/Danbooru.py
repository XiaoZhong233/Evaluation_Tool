#split file for DanbooRegion2020
from PIL import Image
from tqdm import tqdm
from util.utils import makeDatasetList_dir, makeDatasetList, openImage, num2tuple, center_crop_and_resize
import os

# resize should be a int or int tuple
def splitFile(root, desc, resize=None, crop=True):
    imgs = makeDatasetList(root)

    for img in tqdm(imgs):
        dir = os.path.basename(os.path.dirname(img))
        name = os.path.basename(img)
        if name.split('.')[-2] != 'image':
            continue
        desc_dir = os.path.join(desc,dir)
        os.makedirs(desc_dir,exist_ok=True)
        file_path = os.path.join(desc_dir,name)

        img = openImage(img)
        # resize
        if not resize is None:
            if crop:
                # do crop
                img = center_crop_and_resize(img,size=resize)
            else:
                # resize
                img = img.resize(num2tuple(resize),resample=Image.ANTIALIAS)

        img.save(file_path)



if __name__ == '__main__':
    root = r'C:\Users\zhw\Desktop\数据\DanbooRegion2020\DanbooRegion2020\DanbooRegion2020'
    desc = r'C:\Users\zhw\Desktop\数据\DanbooRegion2020\resize'
    splitFile(root, desc, resize=256)