import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
'''
题目58：同时绘制开盘价与收盘价
'''

df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False # 解决符号问题

df[['收盘价(元)','开盘价(元)']].plot()
plt.show()