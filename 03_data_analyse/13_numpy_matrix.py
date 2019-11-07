"""
    演示矩阵运算
"""
import numpy as np


ary = np.arange(1,7).reshape(2,3)
print(ary,type(ary))

# matrix构造矩阵 copy字段默认为True：深拷贝  False为浅拷贝
m = np.matrix(ary,copy=True)
print(m,type(m))
ary[0][0] = 3
print(ary,m)

# mat构造矩阵 与源数据共享：浅拷贝
n = np.mat(ary)
print(ary)
