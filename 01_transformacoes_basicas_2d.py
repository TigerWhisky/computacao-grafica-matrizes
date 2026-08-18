from src.vector import Vector
from src.transforms_2d import translation_matrix, rotation_matrix, scaling_matrix, apply_transform
import matplotlib.pyplot as plt

# Ponto original
p = Vector([2, 1])

# Transformações
T = translation_matrix(3, 2)
R = rotation_matrix(45)
S = scaling_matrix(2, 0.5)

# Aplicar
p_t = apply_transform([p], T)[0]
p_r = apply_transform([p], R)[0]
p_s = apply_transform([p], S)[0]

print("Original:   ", p)
print("Translação: ", p_t)
print("Rotação 45°:", p_r)
print("Escala:     ", p_s)
