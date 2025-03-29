"""
数据排序（Sorting）
排序是指将数据按某个列的值进行升序或降序排列。
Pandas 提供了两种主要的方法来进行排序：sort_values() 和 sort_index()。

排序方法
sort_values()：根据列的值进行排序。
sort_index()：根据行或列的索引进行排序。
"""
import pandas as pd

# 示例数据
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 15, 40],
        'Salary': [50000, 60000, 70000, 80000]}

df=pd.DataFrame(data)
# 按照 "Age" 列的值进行降序排序
df_sorted=df.sort_values(by=['Age'],ascending=False)
print(f"按Age列排序后结果：\n{df_sorted}")

# 按照索引进行排序
df_index_sorted=df.sort_index(axis=1)
print(f"按索引排序后结果:\n{df_index_sorted}")