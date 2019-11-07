"""
    使用numpy的vectorize函数 将python函数的参数转换为矢量
"""
import numpy as np

def foo(x,y):
    return x**2 + y**2

print(foo(1,2))

foo_vec = np.vectorize(foo)
print(foo_vec([1,1,1],[2,2,2,]))