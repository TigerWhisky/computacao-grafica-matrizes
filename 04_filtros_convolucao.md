# Filtros de Imagem por Convolução

A convolução é uma operação fundamental em processamento de imagem.

Dado um **kernel** (matriz pequena), deslizamos essa matriz sobre a imagem e calculamos a soma ponderada dos píxeis vizinhos.

## Kernels clássicos implementados

| Kernel     | Efeito                    |
|------------|---------------------------|
| Blur       | Suavização (média)        |
| Sharpen    | Realce de nitidez         |
| Edge       | Deteção de contornos      |
| Sobel X/Y  | Gradientes (bordas)       |
