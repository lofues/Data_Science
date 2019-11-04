"""
    演示matplotlib的动画功能
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma
import random

def update(number):
    print(number)
    mp.text(random.random(),random.random(),number)

mp.figure("a")
a = ma.FuncAnimation(mp.gcf(),update,interval=30)

mp.show()