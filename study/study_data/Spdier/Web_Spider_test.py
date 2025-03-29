# -*- codeing = utf-8 -*-
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
#import sqlite3  # 进行SQLite数据库操作

"""
网页元素示例：
<a href="https://movie.douban.com/subject/1305487/">
                            <span class="title">猫鼠游戏</span>
                                 
<span class="rating_num" property="v:average">9.7</span>
<span>3145346人评价</span>
<p class="quote">
                                <span>希望让人自由。</span>
                            </p>
"""
# 定义正则表达式，用于提取网页中的特定内容
findLink = re.compile(r'<a href="(.*?)">')  # 匹配电影详情链接
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # 匹配图片链接，re.S使.匹配包括换行符在内的所有字符
findTitle = re.compile(r'<span class="title">(.*)</span>')  # 匹配电影标题
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')  # 匹配电影评分
findJudge = re.compile(r'<span>(\d*)人评价</span>')  # 匹配评价人数，\d*匹配任意数量的数字
findInq = re.compile(r'<span class="inq">(.*)</span>')  # 匹配电影概述
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)  # 匹配电影相关信息，如导演、演员等


def main():
    baseurl = "https://movie.douban.com/top250?start="  # 豆瓣电影Top250的基础URL
    # 1.爬取网页数据
    datalist = getData(baseurl)
    savepath = "./output/豆瓣电影Top250.xls"  # 保存Excel文件的路径
    # dbpath = "movie.db"  # 数据库文件路径（未使用）
    # 3.保存数据到Excel
    saveData(datalist, savepath)  # 调用保存数据的函数
    # saveData2DB(datalist, dbpath)  # 保存到数据库的函数（未使用）


# 爬取网页数据并解析
def getData(baseurl):
    datalist = []  # 创建空列表，用于存储所有电影信息
    for i in range(0, 10):  # 循环10次，获取10页数据（每页25条，共250条）
        url = baseurl + str(i * 25)  # 构造完整URL，每页显示25条数据
        html = askURL(url)  # 调用askURL函数获取网页源码
        
        # 2.解析网页数据
        soup = BeautifulSoup(html, "html.parser")  # 使用BeautifulSoup解析HTML
        for item in soup.find_all('div', class_="item"):  # 查找所有class为"item"的div标签
            data = []  # 创建空列表，用于存储单部电影的所有信息
            item = str(item)  # 将BeautifulSoup对象转换为字符串
            
            # 提取电影详情链接
            link = re.findall(findLink, item)[0]  # 使用正则表达式提取链接
            data.append(link)  # 将链接添加到data列表
            
            # 提取图片链接
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            
            # 提取电影标题（可能有中文和外文两个标题）
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):  # 如果有两个标题（中文和外文）
                ctitle = titles[0]  # 中文标题
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  # 外文标题，去除斜杠
                data.append(otitle)
            else:  # 如果只有一个标题
                data.append(titles[0])  # 添加中文标题
                data.append(' ')  # 外文标题位置添加空格
            
            # 提取电影评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            
            # 提取评价人数
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            
            # 提取电影概述
            inq = re.findall(findInq, item)
            if len(inq) != 0:  # 如果找到概述
                inq = inq[0].replace("。", "")  # 去除句号
                data.append(inq)
            else:  # 如果没有概述
                data.append(" ")  # 添加空格
            
            # 提取电影相关信息（导演、演员等）
            # 修复列表索引超出范围的问题
            bd_result = re.findall(findBd, item)
            if len(bd_result) > 0:  # 检查是否找到匹配项
                bd = bd_result[0]
                # 修复无效转义序列的问题
                bd = re.sub(r'<br(\s+)?/>(\s+)?', "", bd)  # 使用r前缀创建原始字符串，替换HTML中的<br/>标签
                bd = re.sub('/', "", bd)  # 去除斜杠
                data.append(bd.strip())  # 去除首尾空白字符后添加到data列表
            else:
                data.append(" ")  # 如果没有找到匹配项，添加空格
            
            datalist.append(data)  # 将当前电影的所有信息添加到总列表中

    return datalist  # 返回包含所有电影信息的列表


# 获取指定URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        # 用户代理(User-Agent)，模拟浏览器身份
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }
    # 用户代理是爬虫与反爬虫斗争的关键，伪装成浏览器访问可以避免一些基本的反爬机制

    request = urllib.request.Request(url, headers=head)  # 创建请求对象，添加头部信息
    html = ""  # 初始化空字符串，用于存储网页内容
    try:
        response = urllib.request.urlopen(request)  # 发送请求获取响应
        html = response.read().decode("utf-8")  # 读取响应内容并按UTF-8解码
    except urllib.error.URLError as e:  # 捕获URL错误异常
        if hasattr(e, "code"):  # 如果异常对象有code属性（HTTP错误码）
            print(e.code)  # 打印HTTP错误码
        if hasattr(e, "reason"):  # 如果异常对象有reason属性（错误原因）
            print(e.reason)  # 打印错误原因
    return html  # 返回获取到的网页内容


# 保存数据到Excel表格
def saveData(datalist, savepath):
    print("save.......")  # 打印提示信息，表示开始保存数据
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建Excel工作簿对象，使用UTF-8编码
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 创建名为'豆瓣电影Top250'的工作表，允许覆盖单元格
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")  # 定义列名元组
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 写入列名到第一行
    for i in range(0, 250):
        # print("第%d条" %(i+1))  # 输出进度信息（已注释）
        data = datalist[i]  # 获取当前电影数据
        for j in range(0, 8):
            sheet.write(i+1, j, data[j])  # 写入数据到对应单元格，行号从1开始（第0行是列名）
    book.save(savepath)  # 保存Excel文件到指定路径

# 以下是保存数据到SQLite数据库的函数（已注释，未使用）
# def saveData2DB(datalist,dbpath):
#     init_db(dbpath)  # 初始化数据库
#     conn = sqlite3.connect(dbpath)  # 连接到SQLite数据库
#     cur = conn.cursor()  # 获取游标对象
#     for data in datalist:  # 遍历所有电影数据
#             for index in range(len(data)):
#                 if index == 4 or index == 5:  # 跳过评分和评价数（数值类型）
#                     continue
#                 data[index] = '"'+data[index]+'"'  # 为字符串类型数据添加双引号
#             sql = '''
#                     insert into movie250(
#                     info_link,pic_link,cname,ename,score,rated,instroduction,info)
#                     values (%s)'''%",".join(data)  # 构造SQL插入语句
#             # print(sql)  # 输出SQL语句（已注释）
#             cur.execute(sql)  # 执行SQL语句
#             conn.commit()  # 提交事务
#     cur.close  # 关闭游标（注意：这里应该是cur.close()，有一个小bug）
#     conn.close()  # 关闭数据库连接


# 初始化数据库函数（已注释，未使用）
# def init_db(dbpath):
#     sql = '''
#         create table movie250(  # 创建movie250表
#         id integer  primary  key autoincrement,  # 自增主键
#         info_link text,  # 电影详情链接
#         pic_link text,  # 图片链接
#         cname varchar,  # 中文名
#         ename varchar,  # 外文名
#         score numeric,  # 评分
#         rated numeric,  # 评价人数
#         instroduction text,  # 概述
#         info text  # 相关信息
#         )
#
#
#     '''  # 创建数据表的SQL语句
#     conn = sqlite3.connect(dbpath)  # 连接到SQLite数据库
#     cursor = conn.cursor()  # 获取游标对象
#     cursor.execute(sql)  # 执行SQL语句创建表
#     conn.commit()  # 提交事务
#     conn.close()  # 关闭数据库连接

# 保存数据到数据库



if __name__ == "__main__":  # 当程序直接执行时（而非被导入为模块）
    # 调用函数
     main()  # 执行主函数
    # init_db("movietest.db")  # 初始化数据库（已注释，未使用）
     print("爬取完毕！")  # 打印完成提示

