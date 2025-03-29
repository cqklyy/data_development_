import numba
import pandas as pd

# 示例函数
@numba.jit
def calculate_square(x):
    return x ** 2

# 使用 numba 加速计算
df = pd.DataFrame({'A': [1, 2, 3, 4]})
df['B'] = df['A'].apply(calculate_square)
print(df)