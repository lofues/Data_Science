import numpy as np
import matplotlib.pyplot as mp
import math

# 从-pi 到 pi拆分1000个点
x = np.linspace(-np.pi,np.pi,1000)
sinx = np.sin(x)

# y = cos(x)/2
# cosx = -1 * np.cos(x+np.pi/2)
# sin2x = np.sin(2*x)
cosx = np.cos(x)/2

# 控制显示区间
# mp.xlim(0,np.pi)
# mp.ylim(0,1)

# 修改x轴的刻度 指定值 和 坐标文本->laTex文本语法
x_vals = [-np.pi,-np.pi/2,0,np.pi/2,np.pi]
texts = [r'$-\pi$',r'$-\frac{\pi}{2}$','0',r'$\frac{\pi}{2}$',r'$\pi$']
mp.xticks(x_vals,texts)
mp.yticks([-1.0,-0.5,0.5,1])

# 设置坐标轴
# 获取当前坐标轴字典 left right bottom top
ax = mp.gca() # getCurrentAxis

# 上轴与右轴消失  左轴与下轴为0
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')




# linestyle
mp.plot(x,sinx,linestyle=':',linewidth=2,color='red',alpha=0.8,
        label=r'$y=sin(x)$')
mp.plot(x,cosx,linestyle='--',linewidth=2,color='orange',alpha=0.8,
        label=r'$y=\frac{1}{2}cos(x)$')

# 特殊点 s:尺寸 zorder:显示顺序 marker:形状 edgecolors:外边颜色 facecolor:内部颜色
mp.scatter([np.pi/2,np.pi/2],[0,1],
           zorder=3,s=[120,60],marker='o',edgecolors='red',facecolor='blue')

# 给特殊点添加备注
mp.annotate(
    r'$[\frac{\pi}{2},1]$',
    xycoords='data',xy=(np.pi/2,1),
    textcoords='offset points',xytext=(50,-20),
    fontsize=14,arrowprops=dict(
        arrowstyle='->',
        connectionstyle='angle3'
    )
)
mp.annotate(
    r'$[\frac{\pi}{2},0]$',
    xycoords='data',xy=(np.pi/2,0),
    textcoords='offset points',xytext=(-50,-30),
    fontsize=14,arrowprops=dict(
        arrowstyle='->',
        connectionstyle='angle'
    )
)

mp.title('sin and cos function')
mp.xlabel('x axis')
mp.ylabel('y axis')

# 显示label图列的显示位置,默认为best, lebel名称在plot参数中传递
mp.legend()
mp.show()