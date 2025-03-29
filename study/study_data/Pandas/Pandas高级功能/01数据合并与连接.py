import pandas as pd

# 示例数据
left = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']},index=[0,1,2])
right = pd.DataFrame({'Age': [24, 27, 22]},index=[1,2,3])

# 使用 merge（） 进行内连接,如果用how='left'/'right'则是以哪一遍为基准连接
# result = pd.merge(left, right, on='ID', how='inner')

# concat() 用于将多个 DataFrame 沿指定轴（行或列）进行连接，常用于行合并（垂直连接）或列合并（水平连接）
# result=pd.concat([left,right],axis=1,ignore_index=True)

# 使用join（）连接
result=left.join(right,how='inner')

print(result)