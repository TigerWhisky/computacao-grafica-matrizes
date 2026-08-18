"""
Transformações geométricas 2D usando coordenadas homogéneas
"""

import math
from .matrix import Matrix
from .vector import Vector

def translation_matrix(tx: float, ty: float) -> Matrix:
    return Matrix([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def scaling_matrix(sx: float, sy: float) -> Matrix:
    return Matrix([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

def rotation_matrix(angle_degrees: float) -> Matrix:
    angle = math.radians(angle_degrees)
    c, s = math.cos(angle), math.sin(angle)
    return Matrix([
        [c, -s, 0],
        [s,  c, 0],
        [0,  0, 1]
    ])

def shear_matrix(shx: float, shy: float) -> Matrix:
    return Matrix([
        [1, shx, 0],
        [shy, 1, 0],
        [0, 0, 1]
    ])

def apply_transform(points: list[Vector], matrix: Matrix) -> list[Vector]:
    """Aplica transformação a uma lista de pontos 2D"""
    result = []
    for p in points:
        homog = p.to_homogeneous()
        transformed = matrix * homog
        result.append(transformed.from_homogeneous())
    return result
