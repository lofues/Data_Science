import numpy as np

arr = np.random.randint(0,100,(5,5))
print(arr)

# 多维数组的切片[行,列]
print(arr[0][:-4:-1])
# 以逗号为分割，前两行前两列
print(arr[:2,:2])

