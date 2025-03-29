import pandas as pd

# 生成时间序列
date_range = pd.date_range(start='2024-01-01', periods=7, freq='D')
"""
start:起始日期
end：结束日期
periods：生成的时间点数
freq：频率（如 D 表示天，H 表示小时等）
"""
print(date_range)

# 日期偏移
date = pd.to_datetime('2024-01-01')
new_date = date + pd.Timedelta(days=10)
print(new_date)