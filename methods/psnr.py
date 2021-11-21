import numpy as np
import math
from skimage.metrics import peak_signal_noise_ratio
from util.utils import makeDatasetList, openImage


def psnr(img1, img2):
    mse = np.mean( (img1/1.0 - img2/1.0) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def psnr2(img1, img2):
   mse = np.mean( (img1/255. - img2/255.) ** 2 )
   if mse < 1.0e-10:
      return 100
   PIXEL_MAX = 1
   return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def compute_statistics_of_path(real_root, fake_root):
    real_imgs = makeDatasetList(real_root)
    fake_imgs = makeDatasetList(fake_root)
    couple = zip(real_imgs, fake_imgs)
    psnr_ = 0.0
    for r,f in couple:
        r_img = np.array(openImage(r))
        f_img = np.array(openImage(f))
        p = peak_signal_noise_ratio(image_true=r_img,image_test=f_img)
        psnr_ += p
    return psnr_/len(real_imgs)

if __name__ == '__main__':
    real_path = '../dataset/real'
    fake_path = '../dataset/fake'
    psnr = compute_statistics_of_path(real_path,fake_path)
    print(psnr)