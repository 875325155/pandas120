import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目7：提取popularity列中值大于3的行
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "popularity": [1,2,np.nan,4,5,6,7,10]})

print(df[df['popularity']>3])