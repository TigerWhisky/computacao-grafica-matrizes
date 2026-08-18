# Transformações Geométricas 2D

As transformações geométricas 2D são realizadas através de **matrizes 3×3** usando **coordenadas homogéneas**.

## Coordenadas Homogéneas

Um ponto 2D \((x, y)\) é representado como \((x, y, 1)\).

Isto permite que **translações** sejam expressas como multiplicação de matrizes (o que não seria possível com matrizes 2×2).

## Transformações Fundamentais

### Translação
\[
T(t_x, t_y) = \begin{bmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{bmatrix}
\]

### Escala
\[
S(s_x, s_y) = \begin{bmatrix}
s_x & 0 & 0 \\
0 & s_y & 0 \\
0 & 0 & 1
\end{bmatrix}
\]

### Rotação (sentido anti-horário)
\[
R(\theta) = \begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
\]

### Shear (cisalhamento)
\[
Sh(sh_x, sh_y) = \begin{bmatrix}
1 & sh_x & 0 \\
sh_y & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\]

## Composição de Transformações

A ordem **importa**.  
A matriz final é obtida por multiplicação (da direita para a esquerda na ordem de aplicação desejada).

Exemplo:
```python
M = T * R * S   # primeiro escala, depois roda, depois translada
