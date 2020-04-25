import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目4：修改第二列列名为'popularity'
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "score": [1,2,np.nan,4,5,6,7,10]})
df.rename(columns={'score':'popularity'}, inplace = True)
print(df)