from typing import List, Union
from .vector import Vector

class Matrix:
    def __init__(self, data: List[List[float]]):
        self.data = [[float(x) for x in row] for row in data]
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __repr__(self):
        return "Matrix(\n  " + "\n  ".join(str(row) for row in self.data) + "\n)"

    def __mul__(self, other: Union["Matrix", Vector]) -> Union["Matrix", Vector]:
        if isinstance(other, Vector):
            return self._mul_vector(other)
        return self._mul_matrix(other)

    def _mul_vector(self, v: Vector) -> Vector:
        result = []
        for i in range(self.rows):
            s = sum(self.data[i][j] * v.data[j] for j in range(self.cols))
            result.append(s)
        return Vector(result)

    def _mul_matrix(self, other: "Matrix") -> "Matrix":
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                s = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                row.append(s)
            result.append(row)
        return Matrix(result)

    @staticmethod
    def identity(n: int) -> "Matrix":
        return Matrix([[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)])

    def transpose(self) -> "Matrix":
        return Matrix([[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)])
