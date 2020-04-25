import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目20：统计grammer列每个字符串的长度
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "popularity": [1,2,np.nan,4,5,6,7,10]})
df['grammer'] = df['grammer'].fillna('R')
df['len_str'] = df['grammer'].map(lambda x: len(x))
print(df)