import pandas as pd

# 创建 DataFrame
data = {
    'Name': ['ljj', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data,index=[1,2,3,4])

# # 查看前两行数据
# print("前两行数据：","/n",df.head(2))
# print("------")
# # 查看 DataFrame 的基本信息
# print(df.info())
# print("------")
# # 获取描述统计信息
# print("描述统计信息：",df.describe())
#
# # 按年龄排序
# df_sorted = df.sort_values(by='Age', ascending=False)
# print(df_sorted)
#
# # 选择指定列
# print(df[['Name', 'Age']])
#
# # 按索引选择行
# print(df.iloc[1:3])  # 选择第二到第三行（按位置）
#
# # 按标签选择行
# print(df.loc[1:2])  # 选择第二到第三行（按标签）
#
# # 计算分组统计（按城市分组，计算平均年龄）
# print(df.groupby('City')['Age'].mean())
#
# # 处理缺失值（填充缺失值）
# df['Age'] = df['Age'].fillna(30)
#
# # 导出为 CSV 文件
# df.to_excel('D:/study_py/output/pandas_out/df_test.xlsx', index=True)

# # 使用concat添加新行
# new_row = pd.DataFrame([[4, 7]], columns=['A', 'B'])  # 创建一个只包含新行的DataFrame
# df = pd.concat([df, new_row], ignore_index=True)  # 将新行添加到原始DataFrame
#
# # 删除列，axis是指定方向   axis=0：删除行；axis=1：删除列
# df_dropped = df.drop('A',axis=1)
#
# print(df_dropped)

print(df)
print("---------")
# 索引和切片
print(df[['Name', 'Age']])  # 提取多列
print("---------")
print(df[1:3])               # 切片行
print("---------")
print(df.loc[:, 'Name'])     # 提取单列
print("---------")
print(df.loc[1:2, ['Name', 'Age']])  # 标签索引提取指定行列
print("---------")
print(df.iloc[:, 1:])        # 位置索引提取指定列

