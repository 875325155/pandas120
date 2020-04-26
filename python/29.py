import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目29：按照salary列对数据降序排列
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
df.sort_values('salary', ascending=False,inplace=True)
print(df)