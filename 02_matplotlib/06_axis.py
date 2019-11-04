import numpy as np
import matplotlib.pyplot as mp

ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
# 只查看x轴的1 到 10
mp.xlim(1,10)
# 不查看y轴
mp.yticks([])
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0.5))

mp.tight_layout()
mp.show()