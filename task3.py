import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def rgb_to_hsv(arr):
    R, G, B = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    MAX = np.maximum(np.maximum(R, G), B)
    MIN = np.minimum(np.minimum(R, G), B)
    C = MAX - MIN
    C_safe = np.where(C == 0, 1, C)

    H = np.zeros_like(R)
    m = (MAX == R) & (G >= B); H[m] = 60 * (G[m] - B[m]) / C_safe[m]
    m = (MAX == R) & (G <  B); H[m] = 60 * (G[m] - B[m]) / C_safe[m] + 360
    m = (MAX == G);            H[m] = 60 * (B[m] - R[m]) / C_safe[m] + 120
    m = (MAX == B);            H[m] = 60 * (R[m] - G[m]) / C_safe[m] + 240
    H[MAX == MIN] = 0

    S = np.zeros_like(R)
    m = MAX != 0
    S[m] = 1 - MIN[m] / MAX[m]

    V = MAX.copy()
    return H, S, V


def hsv_to_rgb(H, S, V):
    C = V * S
    X = C * (1 - np.abs((H / 60) % 2 - 1))
    m = V - C
    Rp, Gp, Bp = np.zeros_like(H), np.zeros_like(H), np.zeros_like(H)
    h = H % 360

    m0 = (0   <= h) & (h <  60); Rp[m0]=C[m0]; Gp[m0]=X[m0]; Bp[m0]=0
    m1 = (60  <= h) & (h < 120); Rp[m1]=X[m1]; Gp[m1]=C[m1]; Bp[m1]=0
    m2 = (120 <= h) & (h < 180); Rp[m2]=0;     Gp[m2]=C[m2]; Bp[m2]=X[m2]
    m3 = (180 <= h) & (h < 240); Rp[m3]=0;     Gp[m3]=X[m3]; Bp[m3]=C[m3]
    m4 = (240 <= h) & (h < 300); Rp[m4]=X[m4]; Gp[m4]=0;     Bp[m4]=C[m4]
    m5 = (300 <= h) & (h < 360); Rp[m5]=C[m5]; Gp[m5]=0;     Bp[m5]=X[m5]

    return np.stack([Rp+m, Gp+m, Bp+m], axis=2)



H_shift = int(input('Сдвиг оттенка (0-360): '))
S_scale = float(input('Насыщенность (0-3): '))
V_scale = float(input('Яркость (0-3): '))


img = Image.open('ngg.jpg').convert('RGB')
arr = np.array(img).astype(np.float32) / 255.0

H, S, V = rgb_to_hsv(arr)


H_new = (H + H_shift) % 360
S_new = np.clip(S * S_scale, 0, 1)
V_new = np.clip(V * V_scale, 0, 1)

rgb_new = hsv_to_rgb(H_new, S_new, V_new)
rgb_uint8 = np.clip(rgb_new * 255, 0, 255).astype(np.uint8)


Image.fromarray(rgb_uint8).save('result_hsv.jpg')
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(arr);       axes[0].set_title('Оригинал'); axes[0].axis('off')
axes[1].imshow(rgb_uint8); axes[1].set_title('Результат'); axes[1].axis('off')

plt.show()