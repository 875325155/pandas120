import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目31：计算salary列的中位数
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

print(df['salary'])
print(np.median(df['salary']))