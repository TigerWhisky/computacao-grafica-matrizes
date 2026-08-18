"""
Filtros de imagem por convolução usando matrizes propias
"""

from .matrix import Matrix
from PIL import Image
import numpy as np

def convolve(image_array: np.ndarray, kernel: Matrix) -> np.ndarray:
    """Aplica convolução 2D com o kernel (Matrix)"""
    k = np.array(kernel.data)
    kh, kw = k.shape
    pad_h, pad_w = kh // 2, kw // 2

    if image_array.ndim == 3:  # RGB
        channels = []
        for c in range(image_array.shape[2]):
            channels.append(_convolve_channel(image_array[:, :, c], k, pad_h, pad_w))
        return np.stack(channels, axis=2)
    else:
        return _convolve_channel(image_array, k, pad_h, pad_w)

def _convolve_channel(channel, kernel, pad_h, pad_w):
    h, w = channel.shape
    padded = np.pad(channel, ((pad_h, pad_h), (pad_w, pad_w)), mode="edge")
    output = np.zeros_like(channel)

    for i in range(h):
        for j in range(w):
            region = padded[i:i+kernel.shape[0], j:j+kernel.shape[1]]
            output[i, j] = np.sum(region * kernel)

    return np.clip(output, 0, 255)

# Kernels
KERNEL_BLUR = Matrix([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

KERNEL_SHARPEN = Matrix([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

KERNEL_EDGE = Matrix([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

KERNEL_SOBEL_X = Matrix([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

KERNEL_SOBEL_Y = Matrix([
    [-1, -2, -1],
    [0,  0,  0],
    [1,  2,  1]
])
