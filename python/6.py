import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目6：将空值用上下值的平均值填充
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "score": [1,2,np.nan,4,5,6,7,10]})

# pandas里有一个插值方法，就是计算缺失值上下两数的均值
df['popularity'] = df['popularity'].fillna(df['popularity'].interpolate())