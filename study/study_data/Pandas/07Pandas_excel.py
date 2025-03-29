import pandas as pd
intput_file="input/nba.csv"
output_file="D:/study_py/output/pandas_out/df_test.xlsx"
# # 读取csv文件
# df_csv=pd.read_csv(intput_file,header=0)

# # 将csv文件转换成xlsx文件
# df_csv.to_excel(output_file,sheet_name='test-excel',index=False)

# # 读取xlsx文件
# df_xlsx=pd.read_excel(output_file,header=0)
# print(df_xlsx.to_string())

# # 使用 ExcelFile 加载 Excel 文件
# excel_file = pd.ExcelFile(output_file)
#
# sheet_test=excel_file.sheet_names
#
# # 查看所有表单的名称
# print(sheet_test)
#
# # 读取指定的表单
# print(excel_file.parse(sheet_test))
#
#
# # 关闭文件
# excel_file.close()

df1 = pd.DataFrame([["AAA", "BBB"]], columns=["Spam", "Egg"])
df2 = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])
with pd.ExcelWriter(output_file) as writer:
    df1.to_excel(writer, sheet_name="Sheet1")
    df2.to_excel(writer, sheet_name="Sheet2")

df_read=pd.read_excel(output_file,sheet_name=['Sheet2'])
print(df_read)

with pd.ExcelWriter(output_file, mode="a", engine="openpyxl") as writer:
    df1.to_excel(writer, sheet_name="Sheet3")

# 向同一个工作表写入多个 DataFrame，注意 if_sheet_exists 参数需要设置为 overlay
with pd.ExcelWriter("path_to_file.xlsx",
    mode="a",
    engine="openpyxl",
    if_sheet_exists="overlay",
) as writer:
    df1.to_excel(writer, sheet_name="Sheet1")
    df2.to_excel(writer, sheet_name="Sheet1", startcol=3)