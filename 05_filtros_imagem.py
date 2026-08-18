from PIL import Image
import numpy as np
from src.image_filters import convolve, KERNEL_BLUR, KERNEL_SHARPEN, KERNEL_EDGE

# Carregar imagem (substitui por uma imagem tua ou cria uma de teste)
img = Image.new("RGB", (200, 200), color=(100, 150, 200))
# Desenhar algo simples
for i in range(50, 150):
    for j in range(50, 150):
        img.putpixel((i, j), (255, 255, 0))

arr = np.array(img)

blurred = convolve(arr, KERNEL_BLUR)
sharpened = convolve(arr, KERNEL_SHARPEN)
edges = convolve(arr, KERNEL_EDGE)

Image.fromarray(blurred.astype(np.uint8)).save("blurred.png")
Image.fromarray(sharpened.astype(np.uint8)).save("sharpened.png")
Image.fromarray(edges.astype(np.uint8)).save("edges.png")

print("Filtros aplicados e imagens guardadas.")
