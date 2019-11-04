"""
    ndarray中复合数据类型的存取
"""

import numpy as np

data =[
    ('zs', [81, 82, 23], 13),
    ('ls', [81, 85, 23], 14),
    ('ww', [81, 12, 22], 15),
]
# 第一种设置dtype的方式，不宜读
arr = np.array(data, dtype='U2, 3int32, int32')
print(arr,arr.size,arr.shape)
print(arr[2],arr[2][1],arr[2][1][1])

# 第二种设置dtype的方式
arr = np.array(data,dtype=[
    ('name','str_',1),
    ('scores','int32',3),
    ('age','int32',(1,)),
])
print(arr[2]['scores'])

# 第三种设置dtype的方式
arr = np.array(data,dtype={
    'names': ['name','scores','age'],
    'formats': ['U2','3int32','int32']
})
print(arr[2]['scores'])


# 第四种设置dtype的方式
arr = np.array(data,dtype={
    'name':('U3',0),
    'scores':('3int32',16),
    'age':('int32',28)
})
print(arr[0]['name'],arr.itemsize)

