"""
# 删除包含缺失值的行或列
df.dropna()

# 将缺失值替换为指定的值
df.fillna(0)

# 将指定值替换为新值
df.replace('old_value', 'new_value')

# 检查是否有重复的数据
df.duplicated()

# 删除重复的数据
df.drop_duplicates()

# 选择指定的列
df['column_name']

# 通过标签选择数据
df.loc[row_index, column_name]

# 通过位置选择数据
df.iloc[row_index, column_index]

# 通过标签或位置选择数据
df.ix[row_index, column_name]

# 选择指定的列
df.filter(items=['column_name1', 'column_name2'])

# 选择列名匹配正则表达式的列
df.filter(regex='regex')

# 随机选择 n 行数据
df.sample(n=5)

# 按照指定列进行分组
df.groupby('column_name')

# 对分组后的数据进行聚合操作
df.aggregate('function_name')

# 生成透视表
df.pivot_table(values='value', index='index_column', columns='column_name', aggfunc='function_name')
"""