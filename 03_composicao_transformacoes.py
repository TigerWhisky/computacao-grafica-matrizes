"""
Demonstração da importância da ordem na composição de transformações.
"""

from src.vector import Vector
from src.transforms_2d import translation_matrix, rotation_matrix, scaling_matrix, apply_transform
import matplotlib.pyplot as plt

# Triângulo original
triangle = [
    Vector([0, 0]),
    Vector([2, 0]),
    Vector([1, 1.5]),
    Vector([0, 0])
]

# Transformações individuais
S = scaling_matrix(1.5, 1.5)
R = rotation_matrix(45)
T = translation_matrix(3, 2)

# Duas ordens diferentes
# 1ª: Escala → Rotação → Translação
M1 = T * (R * S)

# 2ª: Translação → Rotação → Escala
M2 = S * (R * T)

transformed1 = apply_transform(triangle, M1)
transformed2 = apply_transform(triangle, M2)

def plot_poly(points, style, label):
    xs = [p.data[0] for p in points]
    ys = [p.data[1] for p in points]
    plt.plot(xs, ys, style, label=label)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plot_poly(triangle, "b-o", "Original")
plot_poly(transformed1, "r-o", "S → R → T")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.title("Ordem: Escala → Rotação → Translação")

plt.subplot(1, 2, 2)
plot_poly(triangle, "b-o", "Original")
plot_poly(transformed2, "g-o", "T → R → S")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.title("Ordem: Translação → Rotação → Escala")

plt.tight_layout()
plt.show()
