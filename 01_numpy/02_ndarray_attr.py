"""
    演示ndarray属性
"""
import numpy as np

# 数组维度操作：shape
arr = np.arange(1,10)
print(arr,arr.shape)

arr.shape = (3,3)
print(arr,arr.shape)

# 数组元素的数据类型 不要使用dtype属性赋值修改 要使用astype()方法
print(arr,arr.dtype)
arr.dtype = 'int32'
print(arr) # 个数变多，内存空间不变

arr = np.arange(1,10)
arr.shape = (3,3)
arr = arr.astype('float32')
print(arr)

# 数组的长度 size:所有元素个数
print(arr,arr.size,len(arr))

# 数组的索引下标操作 [1,2] == [1][2]
print(arr[1][2])
print('arr[1,2]',arr[1, 2])

# 遍历整个数组
arr = np.arange(1,28)
arr.shape = (3,3,3)
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        print()
        for k in range(arr.shape[2]):
            print(arr[i][j][k],end=', ')


