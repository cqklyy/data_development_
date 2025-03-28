"""
单例模式就是对一个类，只获取其唯一的类实例对象，持续复用它
节省内存
节省创建对象
"""

from str_tools_py import str_tool

s1=str_tool
s2=str_tool

print(id(s1))
print(id(s2))
