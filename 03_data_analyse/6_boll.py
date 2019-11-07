"""
    布林带
"""
"""
    移动平均线
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

dates,opening_prices,highest_prices,lowest_prices,closing_prices=\
    np.loadtxt('./da_data/aapl.csv',delimiter=',',usecols=(1,3,4,5,6),
               unpack=True,dtype='U10,f8,f8,f8,f8',
               converters={1:dmy2ymd})

# 绘制收盘价折线图
mp.figure('AAPL',facecolor='lightgray')
mp.title('AAPL',fontsize=18)
mp.xlabel('Date',fontsize=16)
mp.ylabel('Price',fontsize=16)
mp.grid(linestyle=':')
mp.plot(dates,closing_prices,color='dodgerblue',
        label='Closing Prices',linewidth=2,linestyle='--')
# 设置刻度定位器
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%Y/%m/%d'))
ax.xaxis.set_minor_locator(md.DayLocator())
# dates = dates.astype(md.datetime.datetime)
mp.gcf().autofmt_xdate()

# 加权卷积运算 卷积核在运算时需要逆置
weights = np.exp(np.linspace(0,-1,5))
weights_10 = np.exp(np.linspace(0,-1,10))
weights /= weights.sum()

# 计算中轨：加权5日平均线
ma_5_w = np.convolve(closing_prices,weights[::-1],'valid')

# 计算上轨和下轨
std53 = np.zeros(ma_5_w.size,)
for i in range(std53.size):
    std53[i] = closing_prices[i:i+5].std()
upper = ma_5_w + 2 * std53
lower = ma_5_w - 2 * std53

# 绘制三个轨的曲线
mp.plot(dates[4:],ma_5_w,color='orangered',
        label='ma_5_w',linewidth=2,linestyle='--')
mp.plot(dates[4:],upper,color='orangered',
        label='upper',linewidth=2,linestyle='--')
mp.plot(dates[4:],lower,color='orangered',
        label='lower',linewidth=2,linestyle='--')
mp.fill_between(dates[4:],upper,lower,upper>lower,color='orangered',alpha=0.2)

mp.legend()
mp.show()