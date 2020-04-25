import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目9：计算popularity列平均值
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "score": [1,2,np.nan,4,5,6,7,10]})

print(df['score'].mean())
