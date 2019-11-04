import matplotlib.gridspec as gd
import matplotlib.pyplot as plt


plt.figure('GridSpec test',facecolor='lightblue')
gridsub = gd.GridSpec(3,3)
# 合并操作
plt.subplot(gridsub[0,:2])
plt.text(0.5, 0.5, 1, ha='center', va='center', size=36)
plt.xticks([])
plt.yticks([])
plt.subplot(gridsub[1:3,0])
plt.text(0.5, 0.5, 4, ha='center', va='center', size=36)
plt.xticks([])
plt.yticks([])
plt.subplot(gridsub[:2,2])
plt.text(0.5, 0.5, 2, ha='center', va='center', size=36)
plt.xticks([])
plt.yticks([])
plt.subplot(gridsub[2,1:3])
plt.text(0.5, 0.5, 3, ha='center', va='center', size=36)
plt.xticks([])
plt.yticks([])
plt.subplot(gridsub[1,1])
plt.text(0.5, 0.5, 5, ha='center', va='center', size=36)
plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.show()