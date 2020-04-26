import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# df = pd.DataFrame(data)
'''
题目45：检查数据中是否含有任何缺失值
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
# df["new"] = df["salary"] - df[0]
df1 = pd.DataFrame(pd.Series(np.random.randint(1, 10, 135)))

df= pd.concat([df,df1],axis=1)

print(df.isnull().values.any())