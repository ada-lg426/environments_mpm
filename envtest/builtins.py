import numpy as np
from scipy.ndimage import gaussian_filter
from math import pi, exp

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'fun_expo']

def fun_expo(x):
    return pi**2*exp(x)

def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b
