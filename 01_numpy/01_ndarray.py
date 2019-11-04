import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr,type(arr))

# ndarray的运算
arr = arr + 10
print(arr)
arr = arr * 2
print(arr)

# ndarray的相加
arr = arr + arr
print(arr)

# 元素判断
arr = arr > 40
print(arr)

# 构造numpy数组
a = np.arange(0,5,1)
print(a)

# 构造0数组
a = np.zeros((2,3),dtype='float')
print(a)

# 构造1数组
a = np.ones((2,3),dtype='int32')
print(a)

# 构造1数组 仿造其他类型
b = np.arange(0,10,1,)
print(b)
b = b.reshape((2,5))
print(b)
c = np.ones_like(b)
print(c)












