"""
斯皮尔曼等级相关系数（Spearman Correlation）
斯皮尔曼相关系数用于衡量两个变量的单调关系（无论是线性还是非线性），它是基于变量的排名计算的。
斯皮尔曼相关系数的取值范围与皮尔逊相关系数相同：-1 到 1。
"""
import pandas as pd
from nltk import spearman_correlation

# 示例数据
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [45, 35, 65, 75, 85],
    'Age': [-10, 25, 10, 35, 40]
}
df=pd.DataFrame(data)
# 计算spearman相关系数
spearman_correlation=df.corr(method='spearman')
print(spearman_correlation)