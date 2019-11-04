"""
    窗口操作
"""
import matplotlib.pyplot as plt

plt.figure('Figure AAA',facecolor='lightgray')
plt.title('AAA title',fontsize=16)
plt.grid(linestyle=':')

plt.figure('Figure BBB',facecolor='gray')
plt.title('BBB title',fontsize=16)
plt.grid(linestyle='-.')
plt.tight_layout()

plt.figure('Figure AAA')
plt.xlabel('Date',fontsize=14)
plt.ylabel('Price',fontsize=14)
plt.tight_layout()

plt.show()