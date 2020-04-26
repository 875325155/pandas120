import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目27：查看数值型列的汇总统计
'''
# 数据

df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\21-50数据.xlsx')
print(df.describe())