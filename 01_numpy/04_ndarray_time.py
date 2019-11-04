"""
    用numpy来存储时间对象
"""
import numpy as np

dates = np.array(['2011','2011-01-01',
                  '2012','2012-11-11',
                  '2013-11-11 11:11:11'])
print(dates,dates.dtype)
# M8[D] 转为时间类型 精确到Day  M8[M] 精确到Month M8[Y] 精确到Year
dates = dates.astype('M8[M]')
print(dates, dates.dtype)