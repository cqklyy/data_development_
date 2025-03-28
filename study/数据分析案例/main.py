"""
实现步骤
1、设计一个类，可以完成数据的封装
2、设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3、读取文件，生产数据对象
4、进行数据需求的逻辑计算（计算每一天的销售额）
5、通过PyEcharts进行图形绘制
"""


from data_define import Record
from file_define import FileReader,TxtFileReader,JsonFileReader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

txt_file_reader=TxtFileReader("/data_input/数据分析案例/2011年1月销售数据.txt")
json_file_reader=JsonFileReader("/data_input/数据分析案例/2011年2月销售数据JSON.txt")

jan_data:list[Record]=txt_file_reader.read_data()
feb_data:list[Record]=json_file_reader.read_data()

# 将两个月份的数据合并成1个list来存储
all_data=jan_data+feb_data
#开始数值计算
data_dict={}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日期已有记录，所以和老记录做累加
        data_dict[record.date]+=record.money
    else:
        data_dict[record.date]=record.money


# 可视化图表开发
bar=Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")

)
bar.render("每日销售额柱状图.html")