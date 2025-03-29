"""
相关性热图（Correlation Heatmap）
为了更直观地呈现相关性矩阵，可以使用热图（Heatmap）来可视化各个变量之间的相关性。

使用 seaborn 库绘制相关性热图是一个常见的做法。
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {
    'Height': [150, 160, 17, 180, 190],
    'Weight': [45, 55, 15, 75, 85],
    'Age': [20, 25, 30,25, 40]
}
df = pd.DataFrame(data)

# 绘制相关性热图
plt.figure(figsize=(8, 6))
# figsize 是一个元组 (tuple)，它接受两个数值，分别代表图形的宽度和高度，单位是英寸 (inches)
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
# 说明：sns.heatmap() 绘制相关性热图
# annot=True 表示在热图上显示数值
# cmap='coolwarm' 设置颜色范围
# fmt='.2f':  这个参数控制单元格中显示数值的格式。.2f 表示将数值格式化为带两位小数的浮点数。
# vmin=-1, vmax=1 限制颜色范围为 -1 到 1。
plt.title('Correlation Heatmap')
plt.show()
