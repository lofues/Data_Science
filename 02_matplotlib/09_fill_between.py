"""
    在闭合曲线中填充闭合区域
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8*np.pi,8*np.pi,1000)
sin_x = np.sin(x)
cos_x = np.cos(x/2)/2

figure = plt.figure('fill between',facecolor='lightgray')
plt.title('fill',fontsize=18)
plt.grid(linestyle=':')

# 画sinx
plt.plot(x,sin_x,color='dodgerblue',label=r'$y=sin(x)$')
# 画cosx
plt.plot(x,cos_x,color='orangered',label=r'$\frac{1}{2}cos(\frac{x}{2})$')

# 给x和y坐标轴命名
ax = plt.gca()
plt.xlabel('x axis')
plt.ylabel('y axis')

# 填充
plt.fill_between(x,sin_x,cos_x,sin_x>cos_x,
                 color='dodgerblue',alpha=0.2)
plt.fill_between(x,sin_x,cos_x,sin_x<cos_x,
                 color='orangered',alpha=0.2)

# 显示
plt.legend()
plt.tight_layout()
plt.show()