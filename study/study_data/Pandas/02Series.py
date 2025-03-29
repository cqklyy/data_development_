import pandas as pd

# # 创建一个Series对象，指定名称为'A'，值分别为1, 2, 3, 4
# # 默认索引为0, 1, 2, 3
# series = pd.Series([1, 2, 3, 4], name='A')

# # 显示Series对象
# print(series)

# # 如果你想要显式地设置索引，可以这样做：
# custom_index = [0, 1, 2, 3]  # 自定义索引
# series_with_index = pd.Series([1, 2, 3, 4], index=custom_index, name='A')

# # 显示带有自定义索引的Series对象
# print(series_with_index)
# # 通过索引访问元素
# print(series_with_index[1])


# 创建 Series
data = [1, 2, 3, 4, 5, 6]
index = ['a', 'b', 'c', 'd', 'e', 'f']
s = pd.Series(data, index=index)

# 查看基本信息
print("索引：", s.index)
print("数据：", s.values)
print("数据类型：", s.dtype)
print("前两行数据：", s.head(2))

# 使用 map 函数将每个元素加倍
s_doubled = s.map(lambda x: x * 2)
print("元素加倍后：", s_doubled)

# 计算累计和
cumsum_s = s.cumsum()
print("累计求和：", cumsum_s)

# 查找缺失值（这里没有缺失值，所以返回的全是 False）
print("缺失值判断：", s.isnull())

# 排序
sorted_s = s.sort_values()
print("排序后的 Series：", sorted_s)

