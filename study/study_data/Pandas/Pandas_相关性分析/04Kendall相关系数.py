"""
肯德尔秩相关系数（Kendall Correlation）
肯德尔秩相关系数也用于衡量变量之间的单调关系，它是通过计算两个变量排名之间的一致性来得出的。

肯德尔相关系数的计算较为复杂，适用于较小的数据集。
"""
import pandas as pd

# 示例数据
data = {
    'Height': [150, 60, 170, 180, 190],
    'Weight': [45, 55, 65, 35, 85],
    'Age': [20, 25, 10, 35, 40]
}

df = pd.DataFrame(data)

# 计算肯德尔秩相关系数
kendall_correlation = df.corr(method='kendall')
print(kendall_correlation)