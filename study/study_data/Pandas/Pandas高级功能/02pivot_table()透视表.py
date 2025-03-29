import pandas as pd
from dask.dataframe import pivot_table

# 示例数据
data = {'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
        'Category': ['A', 'B', 'A', 'B'],
        'Sales': [100, 150, 200, 250]}
df = pd.DataFrame(data)

# 创建透视表
pivot_table=df.pivot_table(df,index='Date',fill_value=0,\
                           columns='Category',aggfunc={'Sales':['mean']})
print(pivot_table)