def add(num1,num2):
    result=num1+num2
    print(f"{num1}+{num2}={result}")

add(23,45)

def add1(num1,num2):
    """
    add1函数可以接收2个参数，进行两数相加的功能
    :param num1: 形参num1是其中一个参数
    :param num2: 形参num2是另外一个参数
    :return: 返回值是两数相加的结果
    """
    result=num1+num2
    return result
r=add1("1","2")
print(r)