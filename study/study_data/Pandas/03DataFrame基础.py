import pandas as pd

# data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
#
# # 创建DataFrame
# df = pd.DataFrame(data, columns=['Site', 'Age'])
#
# # 使用astype方法设置每列的数据类型
# df['Site'] = df['Site'].astype(str)
# df['Age'] = df['Age'].astype(float)
#
# print(df)
#
# import pandas as pd
#
# data2 = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
#
# df2 = pd.DataFrame(data2)
#
# print (df2)
#
# data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
#
# df = pd.DataFrame(data)
#
# print (df)
# # nan 表示空值
# print(df.isnull())

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])

