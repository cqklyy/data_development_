import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data={
'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]
}

df=pd.DataFrame(data)
# 绘制热力图
sns.heatmap(df.corr(),annot=True,cmap='coolwarm')

# 数据集中所有数值特征之间的散点图矩阵
sns.pairplot(df)

plt.show()