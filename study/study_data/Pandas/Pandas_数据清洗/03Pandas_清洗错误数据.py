import pandas as pd

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)

# print(df.to_string())

df.loc[2,'age']=12111      # 修正数据
for x in df.index:
    if df.loc[x,"age"]>120:
        df.loc[x,'age']=120
        # df.drop(x, inplace=True)      # 删掉那一行


print(df.to_string())