import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目19：对数据按照"popularity"列值的大小进行排序
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "popularity": [3,2,np.nan,4,5,11,7,10]})
df.sort_values("popularity",inplace=True)
print(df)