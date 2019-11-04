"""
    使用matplotlib的动画功能制作100随机泡泡
"""
import numpy as np
import matplotlib.animation as ma
import matplotlib.pyplot as mp

n = 100
dtype = [
    ('position','float',2),
    ('size','float',1),
    ('color','float',4),
    ('growth','float',1)
]
balls = np.zeros(n,dtype=dtype)

balls['position'] = np.random.uniform(size=(n,2))
balls['size'] = np.random.uniform(10,20,size=n)
balls['color'] = np.random.uniform(size=(n,4))
balls['growth'] = np.random.uniform(20,30,size=n)

mp.figure('Bubble',facecolor='lightgray')
mp.title('Bubble',fontsize=18)
mp.xticks([])
mp.yticks([])

sc = mp.scatter(
    balls['position'][:,0],
    balls['position'][:,1],
    s=balls['size'],
    color=balls['color'],
    alpha=0.5
)

def update(number):
    # balls['growth'] = np.random.uniform(20, 30, size=n)
    # balls['position'] = np.random.uniform(size=(n, 2))
    balls['size'] += balls['growth']
    # 删除一个随机气球并重新产生
    index = number%n
    balls[index]['position'] = np.random.uniform(size=(1, 2))
    balls[index]['size'] = np.random.uniform(10, 20, size=1)
    # 重置所有气泡
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])

anim = ma.FuncAnimation(mp.gcf(), update, interval=30)
mp.show()