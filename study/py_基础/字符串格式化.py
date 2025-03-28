name = "陈麒开"
massge = "%s爱李滢滢" % (name)
print(massge)

# %s:字符串占位  %d：整数数字占位  %f:浮点数占位

# 数字精度控制
# 辅助符号“m.n";m:控制宽度，要求是数字，若要求的数字小于数字自身则不生效;.n:控制小数点精度，会进行小数的四舍五入

num1 = 1234
num2 = 123.456
print("num1宽度控制4，结果是：%4d" % num1)
print("num1宽度控制5，结果是：%5d" % num1)
print("num2宽度不控制，结果是：%.2f" % num2)
print("num2宽度控制9，结果是：%9.4f" % num2)

# f"{}"占位
name = "陈麒开"
massge = f"{name}爱李滢滢"
print(massge)

# 制表符

# end=""不换行
print("hello",end="")
print("world",end="")
print()
# \t多行对齐
print("hello \t world")
print("cqk \t lyy")