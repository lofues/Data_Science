"""
    数组的轴向汇总
"""
import numpy as np
import random

data = np.array(list([random.randint(60,100) for i in range(3)] for j in range(10)))

# 均值
print('*'*50)
avg = list(map(lambda x:np.round(np.mean(x),2),data))
print('均值输出：',avg)

# 均值排序
print('*'*50)
sorted_array = sorted(data,key=lambda x:np.mean(x))
print('均值排序输出：',sorted_array)

# 列最大值
print('*'*50)
max_col = []
for j in range(data.shape[1]):
    max_col.append(np.round(np.max(data[:][j]),2))
print('列最大值：',max_col)

# numpy API 轴向汇总
def func(data):
    pass

# 列最大值 axis = 0 表示垂直方向，axis = 1表示水平方向
print('*'*50)
r = np.apply_along_axis(np.max,0,data)
index = np.apply_along_axis(np.argmax,0,data)
print('列最大值：',r)
print('列最大值索引：',index)