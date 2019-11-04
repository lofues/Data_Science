"""
    绘制饼装图
"""
import numpy as np
import matplotlib.pyplot as mp

mp.figure('pie',facecolor='lightgray')
# 整理数据
values = [26,17,21,29,11]
spaces = [0.05,0.01,0.01,0.01,0.01]
labels = ['Python','JavaScript','C++','Java','PHP']
colors = ['dodgerblue','orangered','limegreen','violet','gold']
mp.title('Language Population Pie',fontsize=20)
# 等轴比例 不使用时圆形并不规则
mp.axis('equal')
mp.pie(values,spaces,labels,colors,'%d%%',shadow=True)

mp.legend(loc=2)
mp.show()