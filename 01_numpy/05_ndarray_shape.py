import numpy as np

a = np.arange(1,7)
print(a,a.shape)

# 视图变维 原数据改变视图改变,其实是一种引用
b = a.reshape(2,3)
print(b,b.shape)
a[2] = 100
print(a,b)

# 指定-1 自动计算行列个数
c = a.reshape(-1,2)
print(c)

# ravel 将原数组转换为行向量
d = a.ravel()
print(d)
a[1] = 999
print(a,b,c,d)

# 复制变维
e = a.flatten()
print('-------------')
print(e)
e.shape = (2,3)
a[0] = 100
print(a,e)
print(id(a),id(e))

# 就地变维
print('-'*45)
print(a)
a.shape = (3,2)
print(a)
a.resize(2,3)
print(a)
