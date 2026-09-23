import numpy as np
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

img=Image.open('ngg.jpg').convert('RGB')
arr = np.array(img)
r=arr[:,:,0]
g=arr[:,:,1]
b=arr[:,:,2]

Y1 = 0.3 * r + 0.59 * g + 0.11 * b
Y1= np.clip(Y1, 0, 255).astype(np.uint8)

Y2=0.21*r+0.72*g+0.07*b
Y2= np.clip(Y2, 0, 255).astype(np.uint8)

diff = np.abs(Y1.astype(np.int16) - Y2.astype(np.int16)).astype(np.uint8)
fig, axes = plt.subplots(1, 3, figsize=(20, 5))
axes[0].imshow(Y1, cmap='gray'); axes[0].set_title('NTSC RGB')
axes[1].imshow(Y2, cmap='gray'); axes[1].set_title('sRGB')
axes[2].imshow(diff, cmap='gray'); axes[2].set_title('Разность')
plt.show()



plt.hist(Y1.ravel(), bins=256, range=(0, 256), alpha=0.6, color='blue',  label='NTSC RGB')
plt.xlabel('Интенсивность')
plt.ylabel('Количество пикселей')
plt.show()
plt.hist(Y2.ravel(), bins=256, range=(0, 256), alpha=0.6, color='orange', label='sRGB')
plt.xlabel('Интенсивность')
plt.ylabel('Количество пикселей')
plt.show()