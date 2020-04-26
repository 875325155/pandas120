import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目26：查看索引、数据类型和内存信息
'''
# 数据

df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\21-50数据.xlsx')
print(df.info())