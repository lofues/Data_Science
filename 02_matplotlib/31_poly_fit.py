"""
    使用多项式拟合股票差价
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

dates, bhp_closing_prices = np.loadtxt('./da_data/bhp.csv',
                                       delimiter=',',usecols=(1, 6), unpack=True,
                                       dtype='M8[D], f8', converters={1: dmy2ymd})
vale_closing_prices = np.loadtxt('./da_data/vale.csv', delimiter=',',
                                 usecols=(6), unpack=True)

# 绘图
mp.figure('Diff price',facecolor='lightgray')
mp.title('Diff price',fontsize=18)
mp.xlabel('Date',fontsize=16)
mp.ylabel('Price',fontsize=16)
mp.grid(linestyle=':')
# 设置刻度定位器
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%Y/%m/%d'))
ax.xaxis.set_minor_locator(md.DayLocator())
# dates = dates.astype(md.datetime.datetime)
mp.gcf().autofmt_xdate()

# 计算差价函数并画出
diff_prices = bhp_closing_prices - vale_closing_prices
mp.plot(dates,diff_prices,color='dodgerblue',label='diff price',linewidth=1,linestyle='--')

# 拟合这种数据得到多项式函数方程  画出拟合曲线
x = dates.astype('M8[D]').astype('int32')
y = diff_prices
P = np.polyfit(x,y,4)
predict_y = np.polyval(P,x)
mp.plot(dates,predict_y,color='orangered',label='predict',linewidth=1)

Q = np.polyder(P)
xs = np.roots(Q)
ys = np.polyval(P,xs)
mp.hlines(ys,dates[0],dates[-1],zorder=0.5,color='green',alpha=0.3)

mp.legend()
mp.show()