"""
    位运算
"""
import numpy as np

a = np.array([2,-3,-9,6,-1,2])
b = np.array([3,4,6,2,3,4])
print(a^b<0)


# 利用位与运算计算某个数字是否是2的幂
a = np.arange(2100000)
print(a[a & (a-1)==0])
