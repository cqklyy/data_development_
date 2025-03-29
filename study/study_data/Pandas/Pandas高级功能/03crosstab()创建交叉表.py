import pandas as pd

# 示例数据
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Region': ['North', 'South', 'North', 'South', 'West', 'East']}
df = pd.DataFrame(data)

# 创建交叉表
cross_table = pd.crosstab(df['Category'], df['Region'])
print(cross_table)