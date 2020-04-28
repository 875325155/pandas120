import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
题目57：绘制收盘价的折线图
'''

df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
plt.plot(df['收盘价(元)'])
plt.show()