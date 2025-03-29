"""
数据聚合（Aggregation）
聚合是将数据按某些规则进行汇总，通常是对某些列的数据进行求和、求平均数、求最大值、求最小值等操作。
Pandas 提供了groupby()方法来对数据进行分组，然后应用不同的聚合函数。

聚合方法
groupby()：按某些列分组。
聚合函数：如 sum(), mean(), count(), min(), max(), std() 等。
"""
import pandas as pd

# 示例数据
data = {'Department': ['HR', 'Finance', 'HR', 'IT', 'IT'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Salary': [50000, 60000, 55000, 70000, 75000]}

df = pd.DataFrame(data)

# 按照部门分组，并计算每个部门的平均薪资
grouped_df = df.groupby('Department')['Salary'].mean()
print(grouped_df)

# 按照部门分组后，按薪资降序排序
grouped_sorted = df.groupby('Department').apply(lambda x: x.sort_values(by='Salary', ascending=False))
print(grouped_sorted)

# 按照部门分组，并计算每个部门的薪资的平均值和总和
grouped_multiple = df.groupby('Department').agg({'Salary': ['mean', 'sum']})
print(grouped_multiple)