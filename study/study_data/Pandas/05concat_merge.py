import pandas as pd

data1={
    "column1":[1,2,3],
    "column2":[4,5,6],
}
data2={
    "column1":[1,2,3],
    "column2":[5,6,7],
}
df1=pd.DataFrame(data1,index=[0,1,2])
df2=pd.DataFrame(data2)
print(f"df1=\n{df1}")
print(f"df2=\n{df2}")

df_concat=pd.concat([df1,df2],ignore_index=True)
df_merge=pd.merge(df2,df1,on="column1")

# print(f"纵向合并后：\n{df_concat}")
print(f"横向合并后：\n{df_merge}")