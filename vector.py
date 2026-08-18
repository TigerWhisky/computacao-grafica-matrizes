from typing import List, Union
import math

class Vector:
    def __init__(self, data: List[float]):
        self.data = [float(x) for x in data]
        self.dim = len(self.data)

    def __repr__(self):
        return f"Vector({self.data})"

    def __add__(self, other: "Vector") -> "Vector":
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def __mul__(self, scalar: float) -> "Vector":
        return Vector([x * scalar for x in self.data])

    def __rmul__(self, scalar: float) -> "Vector":
        return self * scalar

    def dot(self, other: "Vector") -> float:
        return sum(a * b for a, b in zip(self.data, other.data))

    def norm(self) -> float:
        return math.sqrt(self.dot(self))

    def to_homogeneous(self) -> "Vector":
        """Converte para coordenadas homogéneas (acrescenta 1)"""
        return Vector(self.data + [1.0])

    def from_homogeneous(self) -> "Vector":
        """Remove a coordenada homogénea (divide por w se necessário)"""
        if abs(self.data[-1]) < 1e-10:
            return Vector(self.data[:-1])
        w = self.data[-1]
        return Vector([x / w for x in self.data[:-1]])
