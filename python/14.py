import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目14：交换两列位置
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "popularity": [1,2,np.nan,4,5,6,7,10]})
temp = df['popularity']
df.drop(labels=['popularity'], axis=1,inplace = True)
df.insert(0, 'popularity', temp)
print(df)