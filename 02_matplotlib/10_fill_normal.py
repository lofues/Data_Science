"""
    填充normal
"""
import numpy as np
import matplotlib.pyplot as mp


x = np.linspace(-5,5,10000)
param = 1/(2*np.pi)**0.5
# 计算y的normal
top = -1/2 * x*x
y = param*np.exp(top)

mp.figure('fill normal',facecolor='lightgrey')
mp.plot(x,y,label='normal')

# 在0,1 1,2 2,3 中填充颜色
y_1 = y[5000:6000]
y_2 = y[6000:7000]
y_3 = y[7000:8000]
mp.fill_between(x[5000:6000],y_1,0,y_1>0,color='orangered',alpha=0.2)
mp.fill_between(x[6000:7000],y_2,0,y_2>0,color='dodgerblue',alpha=0.2)
mp.fill_between(x[7000:8000],y_3,0,y_3>0,color='green',alpha=0.2)

mp.legend()
mp.show()