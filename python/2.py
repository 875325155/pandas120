import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目2：提取含有字符串"Python"的行
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "score": [1,2,np.nan,4,5,6,7,10]})
print(df[df['grammer']=='Python'])