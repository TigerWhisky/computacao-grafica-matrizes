from src.vector import Vector
from src.transforms_2d import translation_matrix, rotation_matrix, scaling_matrix, apply_transform
import math

def test_translation():
    p = Vector([1, 2])
    T = translation_matrix(3, 4)
    result = apply_transform([p], T)[0]
    assert result.data == [4.0, 6.0]

def test_scaling():
    p = Vector([2, 3])
    S = scaling_matrix(2, 0.5)
    result = apply_transform([p], S)[0]
    assert result.data == [4.0, 1.5]

def test_rotation_90():
    p = Vector([1, 0])
    R = rotation_matrix(90)
    result = apply_transform([p], R)[0]
    assert abs(result.data[0] - 0.0) < 1e-10
    assert abs(result.data[1] - 1.0) < 1e-10
