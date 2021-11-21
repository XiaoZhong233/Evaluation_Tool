from util.utils import makeDatasetList, openImage
from skimage.metrics import structural_similarity
import numpy as np
import tqdm
import matplotlib.pyplot as plt

def compute_statistics_of_path(real_root, fake_root):
    real_imgs = makeDatasetList(real_root)
    fake_imgs = makeDatasetList(fake_root)
    couple = zip(real_imgs, fake_imgs)
    ssim = 0.0

    for r,f in couple:
        r_img = np.array(openImage(r))
        f_img = np.array(openImage(f))
        s,si = structural_similarity(im1=r_img,im2=f_img,multichannel=True,full=True)
        # plt.imshow(si)
        # plt.show()
        ssim += s
    return ssim/len(real_imgs)

if __name__ == '__main__':
    real_path = '../dataset/real'
    fake_path = '../dataset/fake'
    ssim = compute_statistics_of_path(real_path,fake_path)
    print(ssim)