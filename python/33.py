import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# df = pd.DataFrame(data)
'''
题目33：绘制薪资水平密度曲线
'''
# 数据

df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\21-50数据.xlsx')
def func(df):
    lst = df['salary'].split('-')
    smin = int(lst[0].strip('k'))
    smax = int(lst[1].strip('k'))
    df['salary'] = int((smin + smax) / 2 * 1000)
    return df

df = df.apply(func,axis=1)
plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False # 解决符号问题

df.salary.plot(kind='kde',xlim = (0,70000))
plt.show()