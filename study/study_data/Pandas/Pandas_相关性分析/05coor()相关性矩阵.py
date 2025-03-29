"""
相关性矩阵
相关性矩阵是一个对称矩阵，矩阵中的每个值表示两个变量之间的相关系数。

可以通过 corr() 方法直接计算 DataFrame 中所有变量的相关性矩阵。

说明：相关性矩阵可以帮助我们快速识别出哪些变量之间有较强的线性或单调关系。
在实际分析中，相关性矩阵对于特征选择和降维非常有帮助。
"""
import pandas as pd

# 示例数据
data = {
    'Height': [150, 60, 170, 180, 190],
    'Weight': [45, 55, 65, 35, 85],
    'Age': [20, 25, 30, 35, 40]
}
df = pd.DataFrame(data)

# 计算相关性矩阵
correlation_matrix = df.corr()
print(correlation_matrix)