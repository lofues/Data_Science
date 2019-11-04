"""
    画三维曲线
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

ax3d = mp.gca(projection='3d')

x,y = np.meshgrid(np.linspace(-3,3,500),
                  np.linspace(-3,3,500))
# z = 10 - x - y
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

ax3d.plot_surface(
    x,
    y,
    z,
    rstride=20,  # 行跨距
    cstride=20,  # 列跨距
    cmap='jet'  # 颜色映射
)
mp.figure('3D Surface',facecolor='lightgray')
mp.title('3D Surface')
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')
mp.tight_layout()

mp.show()