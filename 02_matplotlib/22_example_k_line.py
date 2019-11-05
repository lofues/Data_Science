"""
    绘制k线图
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

# 绘制收盘价折线图
mp.figure('K lines',facecolor='lightgray')
mp.title('K lines',fontsize=18)
mp.xlabel('Date',fontsize=16)
mp.ylabel('Price',fontsize=16)
mp.grid(linestyle=':')
mp.plot(dates,closing_prices,color='dodgerblue',
        label='Closing Prices',linewidth=3,linestyle='--',zorder=1)
# 设置刻度定位器
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%Y/%m/%d'))
ax.xaxis.set_minor_locator(md.DayLocator())
# dates = dates.astype(md.datetime.datetime)
mp.gcf().autofmt_xdate()

# 根据涨跌情况，设置边缘色与填充色 涨:边缘色红 填充色白  跌：边缘色绿 填充色绿
rise = closing_prices > opening_prices
# color = ['white' if x else 'green' for x in rise]
# ecolor = ['red' if x else 'green' for x in rise]

# 方法2
color = np.zeros(rise.size,dtype='U5')
ecolor = np.zeros(rise.size,dtype='U5')
color[:] = 'green'
color[rise] = 'white'
ecolor[:] = 'green'
ecolor[rise] = 'red'

# 绘制k线图
# 绘制实体

# edgecolor：边缘色数组 color：填充色数组
mp.bar(dates,closing_prices-opening_prices,0.8,opening_prices,color=color,edgecolor=ecolor,label='K lines',zorder=3)
# 绘制影线
mp.vlines(dates,lowest_prices,highest_prices,color=color,edgecolor=ecolor)

# 计算收盘价均值 并画水平线段
m = np.mean(closing_prices)
m_ = closing_prices.mean()
print(m)
mp.hlines(m,dates[0],dates[-1],color='orangered',zorder=0.5,label='Mean(cp)',alpha=0.5)

# 计算VWAP 成交量加权平均值
vwap = np.average(closing_prices,weights=volumes)
mp.hlines(vwap,dates[0],dates[-1],color='blue',zorder=0.5,alpha=0.5,label='VWAP')
print(vwap)

# 模拟计算TWAP
weights_t = np.linspace(1,7,closing_prices.size)
twap = np.average(closing_prices,weights=weights_t)
mp.hlines(twap,dates[0],dates[-1],zorder=0.5,label='TWAP',alpha=0.5,color='yellow')

median = np.median(closing_prices)
mp.hlines(median,dates[0],dates[-1],zorder=0.5,label='Median',alpha=0.5,color='grey')

mp.legend()
mp.show()