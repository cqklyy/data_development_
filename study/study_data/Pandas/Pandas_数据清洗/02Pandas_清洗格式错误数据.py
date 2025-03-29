import pandas as pd

# 第三个日期格式错误
data = {
  "Date": ['2020/12/01', '2020/12/02' , '20201226'],
  "duration": [50, 40, 45]
}

df=pd.DataFrame(data,index=['day1','day2','day3'])
# print(df)
# 将列中的所有单元格转换为相同格式的数据
# format='mixed'：pandas 将根据每个元素的具体情况自动推断日期格式。这对于处理包含多种日期格式的列非常有用。
df['Date']=pd.to_datetime(df['Date'],format='mixed',errors='coerce')

print(df.to_string())
