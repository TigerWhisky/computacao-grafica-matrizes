"""
Transformações 3D básicas + projecção perspetiva simples
"""

import math
from .matrix import Matrix
from .vector import Vector

def translation_matrix_3d(tx: float, ty: float, tz: float) -> Matrix:
    return Matrix([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

def scaling_matrix_3d(sx: float, sy: float, sz: float) -> Matrix:
    return Matrix([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])

def rotation_x_matrix(angle_degrees: float) -> Matrix:
    a = math.radians(angle_degrees)
    c, s = math.cos(a), math.sin(a)
    return Matrix([
        [1, 0, 0, 0],
        [0, c, -s, 0],
        [0, s,  c, 0],
        [0, 0, 0, 1]
    ])

def rotation_y_matrix(angle_degrees: float) -> Matrix:
    a = math.radians(angle_degrees)
    c, s = math.cos(a), math.sin(a)
    return Matrix([
        [c, 0, s, 0],
        [0, 1, 0, 0],
        [-s, 0, c, 0],
        [0, 0, 0, 1]
    ])

def perspective_projection_matrix(d: float = 5.0) -> Matrix:
    """Projecção perspetiva simples (câmara em z negativo)"""
    return Matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, -1/d, 0]
    ])
