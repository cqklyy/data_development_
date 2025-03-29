from sklearn.preprocessing import StandardScaler
import pandas as pd

# 示例数据
data = {'Age': [25, 30, 35, 40, 45],
        'Salary': [50000, 60000, 70000, 80000, 90000]}

df = pd.DataFrame(data)

# 标准化数据  将数据转换为均值为0，标准差为1的分布
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

print(df_scaled)