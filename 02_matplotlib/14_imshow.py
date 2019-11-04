import numpy as np
import matplotlib.pyplot as mp

n = 1000
# 生成网格化坐标矩阵
x,y = np.meshgrid(np.linspace(-3,3,n),
                  np.linspace(-3,3,n))
# print(x,y,x.shape,y.shape)

# 根据每个网格点坐标，通过某个公式计算z高度坐标
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

mp.figure('Imshow',facecolor='lightgray')
mp.title('Imshow',fontsize=16)
mp.grid(linestyle=':')
# mp.imshow(z,cmap='jet',origin='low')
mp.imshow(z,cmap='gray',origin='low')
# mp.imshow(z,cmap='gist_rainbow',origin='low')

mp.colorbar()

mp.show()