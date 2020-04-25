import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目1：将下面的字典创建为DataFrame
'''
# 假如是直接创建
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "score": [1,2,np.nan,4,5,6,7,10]})
print(df)