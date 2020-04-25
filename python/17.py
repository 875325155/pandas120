import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目17：删除最后一行数据
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "popularity": [1,2,np.nan,4,5,6,7,10]})
df.drop(labels=df.shape[0]-1,inplace=True)
print(df)