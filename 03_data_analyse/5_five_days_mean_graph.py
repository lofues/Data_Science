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


# 绘制5日移动均线
closing_prices_5,closing_prices_10 = [],[]
for j in range(4,closing_prices.size):
    closing_prices_5.append(np.mean(closing_prices[j-4:j+1]))
for j in range(9,closing_prices.size):
    closing_prices_10.append(np.mean(closing_prices[j-9:j+1]))

# 基于卷积实现5日移动均线，有效卷积
kernal_5 = np.ones(5)/5
kernal_10 = np.ones(10)/10
ma_5 = np.convolve(closing_prices,kernal_5,'valid')
ma_10 = np.convolve(closing_prices,kernal_10,'valid')

# 加权卷积运算 卷积核在运算时需要逆置
weights = np.exp(np.linspace(0,-1,5))
weights_10 = np.exp(np.linspace(0,-1,10))
weights /= weights.sum()
weights_10 /= weights_10.sum()

ma_5_w = np.convolve(closing_prices,weights[::-1],'valid')
ma_10_w = np.convolve(closing_prices,weights_10[::-1],'valid')

mp.plot(dates[4:],ma_5_w,color='orangered',
        label='MA5',linewidth=2,linestyle='--')
mp.plot(dates[9:],ma_10_w,color='yellow',
        label='MA10',linewidth=2,linestyle='--')
mp.legend()
mp.show()