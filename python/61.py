import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
题目61：以data的列名创建一个dataframe
'''
plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False # 解决符号问题
df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
# print(df)
# print(list(df.columns))
temp = pd.DataFrame(columns = list(df.columns))
print(temp)