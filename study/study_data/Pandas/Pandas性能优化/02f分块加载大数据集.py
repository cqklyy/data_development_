import pandas as pd
from semver import process
import dask.dataframe as dd

# 使用 Dask 读取大数据集
df = dd.read_csv('large_file.csv')

# 进行计算操作
df.groupby('category').sum().compute()

# Pandas 提供了 chunksize 参数，允许在读取 CSV 或 Excel 文件时分块加载数据
# 分块读取 CSV 文件
chunksize = 10000
for chunk in pd.read_csv('large_file.csv', chunksize=chunksize):
    # 对每个数据块进行处理
    process(chunk)