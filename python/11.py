import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目11：将DataFrame保存为EXCEL
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "score": [1,2,np.nan,4,5,6,7,10]})

df.to_excel('filename.xlsx')
