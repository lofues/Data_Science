import numpy as np

# bool 掩码 找a数组的偶数
a = np.arange(10)
mask = a % 2 == 0
print(a[mask])

# bool 掩码 找a数组21的共倍数
print('*'*50)
a = np.arange(100)
mask = (a%3==0)&(a%7==0)
print(mask)
print(a[(a%3==0) & (a%7==0)])

# 索引掩码
print('*'*50)
a = np.array([10,20,30,40])
mask = [0,3,2,0,1,2,0,3,1,2,3,0,2]
b = a[mask]
print(b)

# 为商品排序
products = np.array(['Mi','Huawei','Apple','Sansung'])
prices = np.array([2999,4999,8888,3999])

# 为数组排序,并且返回有序索引
indices = np.argsort(prices)
print(indices)
print(products[indices])

