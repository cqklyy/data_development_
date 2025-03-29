import pandas as pd
from xarray.util.generate_ops import inplace

# 示例数据
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

def cloumn_func(x):
    return x*2

df['A']=df['A'].apply(cloumn_func)
# print(df)

# 在 DataFrame 上应用自定义函数
# applymap() — 在整个 DataFrame 上应用函数
df=df.applymap(lambda x:x+1)
# print(df)

# 示例数据
df_map = pd.DataFrame({'A': ['cat', 'dog', 'rabbit']})

# 使用字典进行映射
# map() 可以对 Series 中的每个元素应用一个函数或一个映射关系。
df_map['A'] = df_map['A'].map({'cat': 'kitten', 'dog': 'puppy'})
print(df_map)