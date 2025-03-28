"""
演示Python正则表达式使用元字符进行匹配
"""
import re
# s='cqklyy @@python2 !!666 ##cqk'
#
# result=re.findall(r'[a-zA-Z0-9]',s)
# print(result)

# 匹配账号，只能由字母和数字组成，长度限制6到10位
r='^[0-9a-zA-Z]{6,10}$'
s='166075_'
print(re.findall(r,s))
# 匹配QQ号，要求纯数字，长度5-11，第一位不为0
# 判断整体要加上^$，只判断子串即包不包含则不用加上
r='^[1-9][0-9]{4,11}$'
s='123456'
print(re.findall(r,s))
# 匹配邮箱地址，只允许qq、163、gmail这三种邮箱地址
r=r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)$)'
s='241723401@qq.com'
print(re.match(r,s))