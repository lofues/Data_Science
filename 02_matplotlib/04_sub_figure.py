import numpy
import matplotlib.pyplot as plt

plt.figure('subplot test',facecolor='lightgray')
for i in range(9):
    plt.subplot(3,3,i+1,facecolor='g',title='index{}'.format(i+1))
    plt.text(
        0.5,0.5,i+1,
        ha='center',
        va='center',
        size=36,
        color='white',
        alpha=0.5,
        withdash=False,

    )
    plt.xticks([])
    plt.yticks([])

    # 设置边框
    axs = plt.gca()
    axs.spines['left'].set_color('none')
    axs.spines['right'].set_color('none')
    axs.spines['top'].set_color('none')
    axs.spines['bottom'].set_color('none')


plt.tight_layout()
plt.show()