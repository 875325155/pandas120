import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# df = pd.DataFrame(data)
'''
题目50：提取salary与new列的和大于60000的最后3行
'''
# 数据

df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\21-50数据.xlsx')
def func(df):
    lst = df['salary'].split('-')
    smin = int(lst[0].strip('k'))
    smax = int(lst[1].strip('k'))
    df['salary'] = int((smin + smax) / 2 * 1000)
    return df

rowsums = df[['salary','new']].apply(np.sum, axis=1)
res = df.iloc[np.where(rowsums > 60000)[0][-3:], :]