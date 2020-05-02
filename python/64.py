import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
题目64：重置data的行号
'''

plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False # 解决符号问题
df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
# plt.hist(df['涨跌幅(%)'].dropna(),bins=30)
# plt.show()
# print(df)
'''
修改索引的目的是因为有时我们修改数据会导致索引混乱
'''
df = df.reset_index(drop=True)
print(df)
