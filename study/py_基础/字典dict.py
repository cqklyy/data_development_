stu_score={
    "李滢滢":
        {
            "英语":10,
            "数学":20
        },
    "陈麒开":
        {
            "英语":100,
            "数学":100
        }
}
lyy_score=stu_score["李滢滢"]["英语"]
print(f"李滢滢的英语分数是:{lyy_score}")

keys=stu_score.keys()
print(keys)

# 遍历字典
for key in keys:
    print(f"字典的key是:{key}")
    print(f"字典的value是：{stu_score[key]}")

num=len(stu_score)
print(f"字典的数量是：{num}")

stu_score["lyy"]={"英语":12,"数学":10}

print(f"增加后的字典是：{stu_score.keys()}")

print(f"排序后结果：{sorted(stu_score,reverse=True)}")