import numpy as np
import matplotlib.pyplot as mp

n = 1000
# 生成网格化坐标矩阵
x,y = np.meshgrid(np.linspace(-3,3,n),
                  np.linspace(-3,3,n))
# print(x,y,x.shape,y.shape)

# 根据每个网格点坐标，通过某个公式计算z高度坐标
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

mp.figure('Contour',facecolor='lightgray')
mp.title('Contour',fontsize=16)
mp.xlabel('x',fontsize=14)
mp.ylabel('y',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 给等高线加颜色
mp.contourf(x, y, z, 8, cmap='jet')
# 绘制等高线图
cntr = mp.contour(x, y, z, 20, colors='black',
                  linewidths=0.5)
# 为等高线图添加高度标签
mp.clabel(cntr, inline_spacing=1, fmt='%.1f',
          fontsize=10)
mp.show()