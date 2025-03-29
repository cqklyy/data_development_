import pandas as pd
from xarray.util.generate_ops import inplace

person = {
    "name": ['Google', 'Runoob', 'cqk', 'Taobao'],
    "age": [50, 40, 40, 23]
}
df = pd.DataFrame(person)

# 检查是否有重复值
print(df.duplicated())

df.drop_duplicates(subset=['name'],inplace=True)
print(df)
