from src.image_filters import KERNEL_BLUR, KERNEL_SHARPEN, KERNEL_EDGE
from src.matrix import Matrix

def test_kernels_are_matrices():
    assert isinstance(KERNEL_BLUR, Matrix)
    assert isinstance(KERNEL_SHARPEN, Matrix)
    assert isinstance(KERNEL_EDGE, Matrix)

def test_blur_kernel_sum():
    # O kernel de blur deve somar +- 1
    total = sum(sum(row) for row in KERNEL_BLUR.data)
    assert abs(total - 1.0) < 1e-10
