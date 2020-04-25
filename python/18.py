import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目18：添加一行数据['Perl',6.6]
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "popularity": [1,2,np.nan,4,5,6,7,10]})
row = {'grammer':'Perl','popularity':6.6}
df = df.append(row,ignore_index=True)
print(df)