"""
演示Python的闭包特性
"""

# 简单闭包
# def outer(logo):
#     def inner(msg):
#         print(f"{logo}>{msg}<{logo}")
#
#     return inner
#
# fn1=outer("陈麒开")
# fn1("李滢滢")

# 使用nonlocal关键字修改外部函数的值
# def outer(num1):
#     def inner(num2):
#         nonlocal num1
#         num1+=num2
#         print(num1)
#
#     return inner
#
# fn=outer(20)
# fn(30)
# fn(60)

# 使用闭包实现ATM小案例
def account_create(initial_amount=0):
    def atm(num,deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount+=num
            print(f"存款:+{num},账户余额：{initial_amount}")
        else:
            initial_amount -=num
            print(f"取款:-{num},账户余额：{initial_amount}")
    return atm

atm=account_create(50)
atm(20,deposit=True)
atm(10,deposit=False)

