import numpy as np
from scipy.ndimage import gaussian_filter
from PIL import Image
from matplotlib import pyplot as plt

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'time_travel']

def time_travel(file):
    image = Image.open(file).convert('L')
    plt.imshow(image, cmap= 'gray')
    plt.axis("off")
    plt.show()

def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b
