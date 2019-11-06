"""
    测试多项式函数相关API
"""
import numpy as np
import matplotlib.pyplot as mp

P = [4,3,-10,1,3,4]
# 画出函数图像
x = np.linspace(-10,10,1000)
y = np.polyval(P,x)

mp.grid(linestyle=':')
mp.plot(x,y)

# 画出驻点
Q = np.polyder(P)
xs = np.roots(Q)
ys = np.polyval(P,xs)
mp.scatter(xs,ys,s=80,color='orangered')

mp.show()
