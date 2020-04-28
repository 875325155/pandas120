import pandas as pd
import numpy as np
'''
题目54：提取日期列含有空值的行
'''

df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
print(df[df['日期'].isna()])