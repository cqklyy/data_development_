"""
Pearson 即皮尔逊相关系数，用于衡量了两个变量之间的线性关系强度和方向，
它的取值范围在 -1 到 1 之间，其中 -1 表示完全负相关，1 表示完全正相关，0 表示无线性相关。

Pandas 可以使用 corr() 方法计算数据框中各列之间的 Pearson 相关系数。
"""
import pandas as pd

# 示例数据
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [45, 35, 65, 75, 85],
    'Age': [20, 25, 30, 35, 40]
}
df=pd.DataFrame(data,index=[0,1,2,3,4])
# 计算pearson相关系数
correlation=df.corr(method='pearson')
print(correlation)