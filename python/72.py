import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
题目72：将收盘价5日均线、20日均线与原始数据绘制在同一个图上
'''

plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False # 解决符号问题
df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
lst = []
for index,row in df.iterrows():
    if type(row[13]) != float:
        lst.append(index)
df.drop(labels=lst,inplace=True)

df['收盘价(元)'].plot()
df['收盘价(元)'].rolling(5).mean().plot()
df['收盘价(元)'].rolling(20).mean().plot()

# print(df['收盘价(元)'].rolling(5).sum())
plt.show()