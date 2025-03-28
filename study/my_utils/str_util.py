def str_reverse(s):
    """
    功能是将字符串完成反转
    :param s: 将被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]

def substr(s,x,y):
    """
    功能是按照下标x，y对字符串进行切片
    :param s: 将被切片的字符串
    :param x: 给定的下标初始
    :param y: 给定的下标结束
    :return: 切片后的字符串
    """
    return s[x:y]

if __name__ =="__main__":
    print(str_reverse("cqklyy"))
    print(substr("cqklyy",1,3))

