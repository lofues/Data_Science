"""
    散点图
"""
import numpy as np
import matplotlib.pyplot as mp

n = 1000
x = np.random.normal(175,7,n)
y = np.random.normal(65,10,n)

mp.figure('Scatter', facecolor='lightgray')
mp.title('Scatter',fontsize=18)
mp.grid(linestyle=':')

# 设置映射 距离中间的距离
d = (x-175)**2 + (y-65)**2
mp.scatter(x,y, marker='o',
           c=d,cmap='jet_r',
           s=70,label='Samples')
mp.legend()
mp.show()