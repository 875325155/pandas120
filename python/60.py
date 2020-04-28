import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
题目60：让直方图更细致
'''

plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False # 解决符号问题
df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
plt.hist(df['涨跌幅(%)'].dropna(),bins=30)
plt.show()