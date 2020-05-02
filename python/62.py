import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
题目62：打印所有换手率不是数字的行
'''

plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False # 解决符号问题
df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
temp = pd.DataFrame(columns = list(df.columns))
for index,row in df.iterrows():
    if type(row[13]) != float:
        temp = temp.append(df.loc[index])
print(temp)