# Transformações Geométricas 3D

No 3D usamos matrizes **4×4** e coordenadas homogéneas \((x, y, z, 1)\).

## Transformações Básicas

- Translação
- Escala
- Rotação em torno dos eixos X, Y e Z

## Projeção Perspetiva

A projeção perspetiva simula a forma como o olho humano vê o mundo (objetos mais longe parecem menores).

Uma matriz de projeção perspetiva simples (câmara a olhar para o eixo Z negativo) é:

\[
P = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & -1/d & 0
\end{bmatrix}
\]

Depois da multiplicação é necessário fazer a **divisão perspetiva** (\(x/w\), \(y/w\)).
