import pandas as pd
import numpy as np
'''
题目52：查看数据前三行
'''

df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
print(df.head(3))