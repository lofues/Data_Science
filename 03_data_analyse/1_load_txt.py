"""
    读取csv文件并分析
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

mp.legend()
mp.show()