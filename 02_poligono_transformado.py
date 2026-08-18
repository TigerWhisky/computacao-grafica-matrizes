from src.vector import Vector
from src.transforms_2d import rotation_matrix, translation_matrix, scaling_matrix, apply_transform
import matplotlib.pyplot as plt

# Quadrado unitário
square = [
    Vector([0, 0]),
    Vector([1, 0]),
    Vector([1, 1]),
    Vector([0, 1]),
    Vector([0, 0])  # fechar
]

# Composição: Escala → Rotação → Translação
S = scaling_matrix(2, 2)
R = rotation_matrix(30)
T = translation_matrix(3, 1)

# Ordem importante: T * R * S
transform = T * (R * S)

transformed = apply_transform(square, transform)

# Visualização
def plot_poly(points, style, label):
    xs = [p.data[0] for p in points]
    ys = [p.data[1] for p in points]
    plt.plot(xs, ys, style, label=label)

plt.figure(figsize=(8, 6))
plot_poly(square, "b-o", "Original")
plot_poly(transformed, "r-o", "Transformado")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.title("Transformação de Polígono com Matrizes")
plt.show()
