import pandas as pd
import numpy as np
'''
题目56：删除所有存在缺失值的行
'''

df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\51-80数据.xls')
df.dropna(axis=0, how='any', inplace=True)
'''
axis：0-行操作（默认），1-列操作
how：any-只要有空值就删除（默认），all-全部为空值才删除
inplace：False-返回新的数据集（默认），True-在原数据集上操作
'''
print(df)