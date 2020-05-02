import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
题目78：绘制上一题的移动均值与原始数据折线图
'''

plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False # 解决符号问题
df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
lst = []
for index,row in df.iterrows():
    if type(row[13]) != float:
        lst.append(index)
df.drop(labels=lst,inplace=True)

df['expanding Open mean']=df['开盘价(元)'].expanding(min_periods=1).mean()
df[['开盘价(元)', 'expanding Open mean']].plot(figsize=(16, 6))
# print(df['收盘价(元)'].rolling(5).sum())
plt.show()