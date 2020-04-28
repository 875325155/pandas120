import pandas as pd
import numpy as np
'''
题目53：查看每列数据缺失值情况
'''

df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
print(df.isnull().sum())