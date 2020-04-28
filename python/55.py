import pandas as pd
import numpy as np
'''
题目55：输出每列缺失值具体行数
'''

df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
for i in df.columns:
    # print(i)
    if df[i].count() != len(df):
        row = df[i][df[i].isnull().values].index.tolist()
        print('列名："{}", 第{}行位置有缺失值'.format(i,row))


