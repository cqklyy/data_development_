"""
演示基础柱状图
"""
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

# 使用Bar构建基础柱状图
bar = Bar()
# 添加x轴
bar.add_xaxis(["中国","美国","英国"])
# 添加y轴
bar.add_yaxis("GDP",[30,10,20],label_opts=LabelOpts(position="right"))
#反转x和y轴
bar.reversal_axis()
#绘图
bar.render("基础柱状图.html")

