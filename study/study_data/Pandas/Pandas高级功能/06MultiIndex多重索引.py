import pandas as pd
from bokeh.util.logconfig import level

# 方法一
# 创建元组
index_tuples = [('A', 1), ('A', 2), ('B', 1), ('B', 2)]

# pd.MultiIndex.from_tuples()，使用元组来创建多重索引，每个元组对应一个索引层级
multi_index = pd.MultiIndex.from_tuples(index_tuples, names=['Letter', 'Number'])
# 创建 DataFrame
df1 = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=multi_index)
# print(df1)

# 方法二
#pd.MultiIndex.from_product()使用多个列表的笛卡尔积来创建多重索引，适合用于数据维度较多的情况
# 创建多个列表
index_values = [['A', 'B'], [1, 2]]

# 创建多重索引
multi_index = pd.MultiIndex.from_product(index_values, names=['Letter', 'Number'])

# 创建 DataFrame
df2 = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=multi_index)
# print(df2)

#使用 set_index() 创建多重索引，可以将 DataFrame 的列转换为多重索引，适用于从已有的数据创建多重索引
# 示例数据
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, 20, 30, 40]
}

df3 = pd.DataFrame(data)

# 设置多重索引
df3.set_index(['Letter', 'Number'], inplace=True)
# print(df3)
print(df3.loc['A',1])

df3_sorted=df3.sort_index(level=['Letter','Number'],ascending=[True,False])
print(df3_sorted)

# 重设索引
df3_reset = df3.reset_index()
print(df3_reset)