def return_test():
    return  1,2
x,y=return_test()
print(f"多参数时返回：{x},{y}")

# 默认参数
def user_info(name,age,gender):
    print(f"姓名：{name},年龄：{age},性别：{gender}")

user_info("cqk",21,"男")

def user_info1(name,age,gender="男"):
    print(f"姓名：{name},年龄：{age},性别：{gender}")

user_info1("cqk",21)
user_info1("cqk",21,gender="女")

# 位置不定长
def user_info2(*args):
    print(f"args的类型是：{type(args)}，内容是：{args}")

user_info2("cqk",111)

# 关键字不定长
def user_info3(**kwargs):
    print(f"kwargs的类型是：{type(kwargs)},内容是：{kwargs}")

user_info3(name="cqk",age=23)