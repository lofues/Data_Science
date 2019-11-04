import numpy as np
import matplotlib.pyplot as mp

x = np.arange(1,11)
y = np.random.randint(1,100,10)
print(x,y)

mp.plot(x,y)
# mp.show()

# 绘制水平线
mp.hlines(60,1,6.5)
# 绘制垂直线 y位置：[]  起始位置:[]  终止位置:[]
mp.vlines([2,4,6,8],[10,20,30,40],[25,35,45,55])
mp.show()

