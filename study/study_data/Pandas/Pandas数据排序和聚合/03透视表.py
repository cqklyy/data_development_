"""
透视表（Pivot Table）是一个特殊的聚合方式，
可以让我们通过行、列和聚合函数对数据进行快速汇总，类似于 Excel 中的透视表
"""
import pandas as pd
from dask.dataframe import pivot_table

data={'Department': ['HR', 'Finance', 'HR', 'IT', 'IT'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Salary': [50000, 60000, 55000, 70000, 75000]
}
df=pd.DataFrame(data)

# fd_agg=df.groupby(['Department']).agg({'Salary':['mean']})
# print(fd_agg)
# 使用 pivot_table 计算每个部门的薪资平均值
pivot_table=df.pivot_table(values='Salary',index='Department',aggfunc=['mean','sum'])
print(pivot_table)