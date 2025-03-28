"""
演示带有时间线的柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType # 导入全局包中的主题类型包

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 10, 20], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 20, 30], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()


bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [70, 30, 40], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 构建时间线对象,以及设置DARK主题
timeline = Timeline({"theme":ThemeType.DARK})
#在时间线添加柱状图对象
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")


#自动播放设置
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

#绘图是用时间线对象绘图，不是用bar对象
timeline.render("基础时间线对象.html")