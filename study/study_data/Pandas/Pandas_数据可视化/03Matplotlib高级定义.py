import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 示例数据
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Sales': [100, 150, 200, 250, 300]}
df = pd.DataFrame(data)

# 绘制折线图
plt.plot(df['Year'], df['Sales'], color='blue', marker='x')

# 自定义
plt.title('Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)      # 添加网格线

# 显示
plt.show()