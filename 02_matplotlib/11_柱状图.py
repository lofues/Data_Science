"""
    绘制柱状图
"""
import numpy as np
import matplotlib.pyplot as mp
import random

mp.figure('Bar Chart',facecolor='lightgray')
mp.subplot(211)
apples = np.array(
    [random.randint(20,100) for _ in range(12)])
mp.title('Bar Chart',fontsize=18)
mp.grid(linestyle=':',axis='x')
mp.xlabel('Month',fontsize=14)
mp.ylabel('Volume',fontsize=14)
x = np.arange(apples.size)
mp.bar(
    x,apples,0.8,color='dodgerblue',
    label='Apple',align='center'
)
mp.xticks(x,['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
mp.legend()

mp.subplot(212)
huawei = np.array(
    [random.randint(20,100) for _ in range(12)])
mp.title('Bar Chart',fontsize=18)
mp.grid(linestyle=':',axis='x')
mp.xlabel('Month',fontsize=14)
mp.ylabel('Volume',fontsize=14)
x = np.arange(apples.size)
mp.bar(
    x-0.2,huawei,0.4,color='orangered',
    label='huawei',align='center'
)
# 错开在一张图中显示两个柱状图
mp.bar(
    x+0.2,apples,0.4,color='dodgerblue',
    label='Apple',align='center'
)
mp.xticks(x,['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

mp.legend()
mp.show()