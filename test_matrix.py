from src.matrix import Matrix
from src.vector import Vector

def test_identity():
    I = Matrix.identity(3)
    assert I.data == [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ]

def test_matrix_vector_mul():
    M = Matrix([
        [1, 2],
        [3, 4]
    ])
    v = Vector([1, 1])
    result = M * v
    assert result.data == [3.0, 7.0]

def test_matrix_mul():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    C = A * B
    assert C.data == [[19.0, 22.0], [43.0, 50.0]]

def test_transpose():
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    At = A.transpose()
    assert At.data == [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]]
