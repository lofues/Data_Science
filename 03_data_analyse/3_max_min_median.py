"""
    计算最大值与最小值，波动性,标准差,中位数
"""

import numpy as np
import matplotlib.pyplot as mp
import datetime
import matplotlib.dates as md

def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    time = datetime.datetime.strptime(dmy, '%d-%m-%Y').date()
    t = time.strftime('%Y-%m-%d')
    return t

dates,opening_prices,highest_prices,lowest_prices,closing_prices,volumes=\
    np.loadtxt('./da_data/aapl.csv',delimiter=',',usecols=(1,3,4,5,6,7),
               unpack=True,dtype='U10,f8,f8,f8,f8,f8',
               converters={1:dmy2ymd})

# 评估30天股价的波动区间
max_val = np.max(highest_prices)
min_val = np.min(lowest_prices)
print(min_val,'~',max_val)

# 找出最大值与最小值的下标 高维只会得到顺序索引
max_index = np.argmax(highest_prices)
min_index = np.argmax(lowest_prices)
median = np.median(closing_prices)
print(min_index,max_index)

# 测试maximum 和minimum
a = np.arange(1,10)
print(a)
b = a[::-1]
print(b)
print(np.maximum(a,b),np.minimum(a,b))

# 测试标准差
std = np.std(closing_prices)
std_ = closing_prices.std()
print(std,std_)

m = np.mean(closing_prices)
d = closing_prices - m
var = np.mean(d**2)
std__ = np.sqrt(var)
print(std__)

# 样本标准差 /n-1
std = np.std(closing_prices,ddof=1)
print(std)
