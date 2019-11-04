"""
    多维数组的组合与拆分
"""
import numpy as np

a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)

print('a->',a)
print('b->',b)

# 垂直组合 vertical
# axis 为0 垂直方向
print('*'*50)
c = np.vstack((a,b))
c = np.concatenate((a,b),axis=0)
print('vertical:',c)

# 水平组合 hiro...
# axis 为1 水平方向
print('*'*50)
d = np.hstack((a,b))
d = np.concatenate((a,b),axis=1)
print('hir:',d)

# 垂直拆分
print('*'*50)
a,b = np.vsplit(c,2)
a,b = np.split(c,2,axis=0)
print('a:',a)
print('b:',b)

# 水平拆分
print('*'*50)
a,b,c = np.hsplit(d,3)
a,b,c = np.split(d,3,axis=1)
print('a:',a)
print('b:',b)
print('c:',c)

# 深度组合
# axis = 2 深度方向组合
e = np.dstack((a,b))
# e = np.concatenate((a,b),axis=2)
print('deep->e:',e)

a,b = np.dsplit(e,2)
print('a:',a)
print('b:',b)

# 长度不等的数组组合
print('*'*50)
a = np.arange(1,6)
b = np.arange(1,4)
# 先在b中前或者后位置上填充元素
b = np.pad(b,pad_width=(1,1),mode='constant',constant_values=0)
c = np.vstack((a,b))
print(c)

# 简单的一维数组组合方案
# 一组x坐标和一组y坐标
x = np.random.randint(1,9,10)
y = np.random.randint(1,9,10)

# 变两行
points = np.row_stack((x,y))
print(points)
# 变两列
points = np.column_stack((x,y))
print(points)
# 通过points(7*2) 拆出x与y坐标数组
x,y = np.hsplit(points,2)
# 7*1
print(x)
print(y)
# 1*7
x = points[:,0]
y = points[:,1]
print(x)
print(y)






