import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as mp

# 生成正太分布随机数
n = 300
x = np.random.normal(0,1,300)
y = np.random.normal(0,1,300)
z = np.random.normal(0,1,300)

mp.figure('3D Scatter',facecolor='lightgray')
mp.subplot(211)
mp.title('3D Scatter',fontsize=18)
# 设置三维坐标系
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('x',fontsize=16)
ax3d.set_ylabel('y',fontsize=16)
ax3d.set_zlabel('z',fontsize=16)
d = x**2 + y**2 + z**2
ax3d.scatter(
    x,
    y,
    z,
    s=80,
    # color='dodgerblue',
    c=d,
    cmap='jet'
)
mp.tight_layout()
mp.show()

mp.subplot(212)
ax3d = mp.gca(projection='3d')
ax3d.plot(x,y,z)
mp.show()
