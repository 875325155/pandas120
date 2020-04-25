import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目10：将grammer列转换为list
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "score": [1,2,np.nan,4,5,6,7,10]})
print(list(df['grammer']))
print(df['grammer'].to_list())
print(type(df['grammer'].to_list()))
