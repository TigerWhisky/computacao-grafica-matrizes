"""
Projeção simples de um cubo 3D para 2D usando matrizes.
"""

from src.vector import Vector
from src.transforms_3d import rotation_y_matrix, rotation_x_matrix, translation_matrix_3d, perspective_projection_matrix
from src.matrix import Matrix
import matplotlib.pyplot as plt

# Vértices de um cubo centrado na origem
cube_vertices = [
    Vector([-1, -1, -1]),
    Vector([ 1, -1, -1]),
    Vector([ 1,  1, -1]),
    Vector([-1,  1, -1]),
    Vector([-1, -1,  1]),
    Vector([ 1, -1,  1]),
    Vector([ 1,  1,  1]),
    Vector([-1,  1,  1]),
]

# Arestas do cubo (pares de índices)
edges = [
    (0,1), (1,2), (2,3), (3,0),  # face traseira
    (4,5), (5,6), (6,7), (7,4),  # face frontal
    (0,4), (1,5), (2,6), (3,7)   # arestas de ligação
]

# Transformações
Ry = rotation_y_matrix(30)
Rx = rotation_x_matrix(20)
T  = translation_matrix_3d(0, 0, 5)          # afastar da câmara
P  = perspective_projection_matrix(d=4.0)

# Matriz final: Projeção * Translação * RotaçãoX * RotaçãoY
MVP = P * (T * (Rx * Ry))

def project(v: Vector) -> tuple:
    """Aplica a matriz e devolve coordenadas 2D"""
    # Converter para homogéneo 4D
    h = Vector(v.data + [1.0])
    transformed = MVP * h
    # Perspetiva divide
    if abs(transformed.data[3]) > 1e-8:
        x = transformed.data[0] / transformed.data[3]
        y = transformed.data[1] / transformed.data[3]
    else:
        x, y = transformed.data[0], transformed.data[1]
    return x, y

# Projetar todos os vértices
projected = [project(v) for v in cube_vertices]

# Desenhar
plt.figure(figsize=(8, 6))
for i, j in edges:
    x_values = [projected[i][0], projected[j][0]]
    y_values = [projected[i][1], projected[j][1]]
    plt.plot(x_values, y_values, "b-", linewidth=1.5)

# Marcar vértices
xs, ys = zip(*projected)
plt.scatter(xs, ys, c="red", s=40)

plt.axis("equal")
plt.grid(True, alpha=0.3)
plt.title("Projeção Perspetiva de um Cubo 3D (apenas com matrizes)")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
