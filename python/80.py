import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
题目73：计算布林指标
'''

plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False # 解决符号问题
df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
lst = []
for index,row in df.iterrows():
    if type(row[13]) != float:
        lst.append(index)
df.drop(labels=lst,inplace=True)

df['former 30 days rolling Close mean']=df['收盘价(元)'].rolling(20).mean()
df['upper bound']=df['former 30 days rolling Close mean']+2*df['收盘价(元)'].rolling(20).std()
df['lower bound']=df['former 30 days rolling Close mean']-2*df['收盘价(元)'].rolling(20).std()
# print(df['收盘价(元)'].rolling(5).sum())
df[['收盘价(元)', 'former 30 days rolling Close mean','upper bound','lower bound' ]].plot(figsize=(16, 6))
plt.show()