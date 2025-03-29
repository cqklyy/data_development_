import pandas as pd
import json
# glom 模块允许我们使用 . 来访问内嵌对象的属性
from glom import glom

# # 读取内嵌的 JSON 数据，会信息显示不全
# df=pd.read_json('D:/study_py/input/nested_list.json')
# print(df)

# # 使用 Python JSON 模块载入数据
# with open('D:/study_py/input/nested_list.json','r') as f:
#     data=json.loads(f.read())

# print(data)

# # 展平数据
# df_nested_list=pd.json_normalize(data,record_path=['students'],meta=['school_name','class'])
# print(df_nested_list)

# # 使用 Python JSON 模块载入数据
# with open('D:/study_py/input/nested_list.json','r') as f:
#     data = json.loads(f.read())
   
# # 使用 json_normalize 展平数据
# df_nested_list = pd.json_normalize(
#     data,
#     record_path=['students'],
#     meta=[
#         'class',
#         ['info', 'president'],
#         ['info', 'contacts']
#     ]
# )

# print("展平后的数据：")
# print(df_nested_list)

# # 方法1：直接使用 DataFrame
# df = pd.DataFrame(data['students'])
# print("\n方法1 - 使用 DataFrame：")
# print(df['math'])

# # 方法2：使用 glom（如果需要的话）
# print("\n方法2 - 使用 glom：")
# math_scores = [glom(student, 'math') for student in data['students']]
# print(math_scores)

# 创建 DataFrame，包含日期数据
df_date = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Date': pd.to_datetime(['2021-01-01', '2022-02-01', '2023-03-01']),
    'Age': [25, 30, 35]
})

# 将 DataFrame 转换为 JSON，并指定日期格式为 'iso'
json_str = df_date.to_json(orient='records',date_format='epoch',lines=True)

print(json_str)