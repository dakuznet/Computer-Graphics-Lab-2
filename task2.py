import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('ngg.jpg').convert('RGB')
img_array = np.array(img)

r = img_array[:, :, 0]
g = img_array[:, :, 1]
b = img_array[:, :, 2]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(r, cmap='gray'); axes[0].set_title('R канал')
axes[1].imshow(g, cmap='gray'); axes[1].set_title('G канал')
axes[2].imshow(b, cmap='gray'); axes[2].set_title('B канал')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(r.ravel(), bins=256, range=(0, 256), alpha=0.6, color='red', label='Red')
plt.hist(g.ravel(), bins=256, range=(0, 256), alpha=0.6, color='green', label='Green')
plt.hist(b.ravel(), bins=256, range=(0, 256), alpha=0.6, color='blue', label='Blue')

plt.title('Гистограммы распределения яркости по каналам')
plt.xlabel('Значение яркости (0-255)')
plt.ylabel('Количество пикселей')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()