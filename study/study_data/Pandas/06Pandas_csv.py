import pandas as pd

df = pd.read_csv('input/nba.csv')

# print(df.to_string())
# print(df)

df.to_csv("output/pandas_out/df_test.csv",index=False,header=True,columns=["Name","Team"])
df_out=pd.read_csv("output/pandas_out/df_test.csv")
print(df_out)
print(f"打印前十行：\n{df_out.head(10)}")
print(f"打印末尾3行：\n{df_out.tail(3)}")
print(f"{df_out.info()}")