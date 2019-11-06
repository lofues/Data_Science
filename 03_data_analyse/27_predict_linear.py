"""
    线性预测 ax1 + bx2 + cx3 = d
"""
import datetime

import matplotlib.dates as md
import matplotlib.pyplot as mp
import numpy as np


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


# 通过前六天的股票价格，整理A与B，得到x
N = 10
pred_prices = np.zeros(closing_prices.size-N*2)
for i in range(pred_prices.size):
    A = np.zeros((N,N))
    for j in range(N):
        A[j,:] = closing_prices[j+i:i+j+N]
    B = closing_prices[N+i:N*2+i]
    x = np.linalg.lstsq(A,B)[0]
    # dot 点积
    pred = B.dot(x)
    pred_prices[i] = pred

mp.plot(dates[N*2:],pred_prices,'o-',
        color='orangered',label='Prediction Price')

mp.legend()
mp.show()