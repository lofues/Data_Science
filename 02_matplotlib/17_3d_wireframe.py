"""
    3d线框图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

ax3d = mp.gca(projection='3d')

x,y = np.meshgrid(np.linspace(0,2,500),
                  np.linspace(0,2,500))
# z = 10 - x - y  # 三维平面
# z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
# z = (x**2 + y**2)**(1/2) # 锥体

mp.figure('3D Surface',facecolor='lightgray')
mp.title('3D Surface',fontsize=18)
ax3d.plot_wireframe(
    x,
    y,
    z,
    rstride=20,  # 行跨距
    cstride=20,  # 列跨距
    color='orangered'
)
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')
mp.tight_layout()

mp.show()