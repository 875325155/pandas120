import numpy as np
import pandas as pd
# df = pd.DataFrame(data)
'''
题目8：按照grammer列进行去重
'''
# 数据
df = pd.DataFrame({
    "grammer": ["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
    "score": [1,2,np.nan,4,5,6,7,10]})
'''
drop_duplicates()的参数构成及其含义。
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
这条语句的含义是按照subset指定的列用keep指定的方法进行去重
    subset：用来指定特定的列，默认是所有列
    keep：指定处理重复值的方法：
        first：保留第一次出现的值
        last：保留最后一次出现的值
        False：删除所有重复值
    inplace：是直接在原来数据上修改还是保留一个副本,为True则修改，否则在False

'''
print(df.drop_duplicates(['grammer']))
