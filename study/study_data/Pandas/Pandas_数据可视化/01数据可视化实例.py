import pandas as pd
import matplotlib.pyplot as plt


# 示例数据
data = {'Year': [2015, 2016, 2017, 2018, 2019, 2020],
        'Sales': [100, 150, 200, 250, 300, 350]}
df = pd.DataFrame(data)

# 绘制折线图
df.plot(kind='line',x='Year',y='Sales',title='Sales over Years',xlabel='Year',ylabel='Sales',\
        figsize=(100,6))
# 绘制柱状图
df.plot(kind='bar',x='Year',y='Sales',title='Sales over Years',xlabel='Year',ylabel='Sales',\
        figsize=(10,6))
# 绘制散点图
df.plot(kind='scatter',x='Year',y='Sales',title='Sales over Year',xlabel='Year',ylabel='Scales',\
        figsize=(10,6))
# 绘制饼图
df.plot(kind='pie', y='Sales', labels=df['Year'], autopct='%1.1f%%',\
        title='Sales over Year', figsize=(8, 5))

plt.show()