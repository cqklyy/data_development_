"""
演示装饰器的写法
"""


# 装饰器的一般写法（闭包）
# def outer(func):
#     def inner():
#         print("我睡觉了")
#         func()
#         print("我醒了")
#
#     return inner
#
#
# def sleep():
#     import random
#     import time
#     print("李滢滢睡觉中...")
#     time.sleep(random.randint(1, 10))
#
#
# fn = outer(sleep)
# fn()

# 装饰器的快捷写法（语法糖）
def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我醒了")

    return inner

@outer
def sleep():
    import random
    import time
    print("李滢滢睡觉中...")
    time.sleep(random.randint(1, 10))


sleep()
