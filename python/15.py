import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目15：提取popularity列最大值所在行
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "popularity": [1,2,np.nan,4,5,6,7,10]})

print(df[df["popularity"]>=max(df["popularity"])])
# df[df['popularity'] == df['popularity'].max()]