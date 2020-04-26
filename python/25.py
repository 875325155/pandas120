import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目25：将createTime列时间转换为月-日
'''
# 数据

df = pd.read_excel(r'E:\Computer Science\Kaggle\Pandas120\pandas120\21-50数据.xlsx')
print(df)
for index,row in df.iterrows():
   df.iloc[index,0] = df.iloc[index,0].to_pydatetime().strftime("%m-%d")
print(df)