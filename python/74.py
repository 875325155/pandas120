import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
题目74：绘制重采样数据与原始数据
'''

plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False # 解决符号问题
df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
lst = []
for index,row in df.iterrows():
    if type(row[13]) != float:
        lst.append(index)
df.drop(labels=lst,inplace=True)

df = df.set_index('日期')
# df['收盘价(元)'].resample('W').max()
# print(df['收盘价(元)'].rolling(5).sum())
# plt.show()
df['收盘价(元)'].plot()
df['收盘价(元)'].resample('7D').max().plot() #重采样
plt.show()
