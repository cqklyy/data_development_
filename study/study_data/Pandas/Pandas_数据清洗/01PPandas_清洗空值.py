import pandas as pd
from statsmodels.sandbox.distributions.genpareto import meanexcess

input_path= '/input/property-data.csv'

missing_value=["na","n/a","--",' ']
df=pd.read_csv(input_path,header=0,na_values=missing_value)
# print(df)

# print(df['NUM_BEDROOMS'])
# print(df['NUM_BEDROOMS'].isnull())

# new_df=df.dropna()
# print(f'去除空值后结果：\n{new_df.to_string()}')
# 默认情况下，dropna() 方法返回一个新的 DataFrame，不会修改源数据。

# 如果你要修改源数据 DataFrame, 可以使用 inplace = True 参数:
# df.dropna(inplace=True)

# print(df['ST_NUM'])
# print(df['ST_NUM'].isnull())
# print(df['ST_NUM'])
x=df['ST_NUM'].mean()
# df['ST_NUM'].fillna(x,inplace=True)
# new_df.dropna(subset=['ST_NUM'])
# print(df.to_string())

y=df['ST_NUM'].mode()
z=df['ST_NUM'].median()
print(f"平均数：{x}")
print(f"众数：{y}")
print(f"中位数：{z}")

