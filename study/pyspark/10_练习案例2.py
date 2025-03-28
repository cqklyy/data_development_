from pyspark import SparkContext,SparkConf
import os
import json
os.environ['PYSPARK_PYTHON']="F:/anaconda/envs/Python37/python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

# 读取文件得到RDD
file_rdd=sc.textFile("F:/pythonProject/data_development/data_input/Spark案例/orders.txt")
# 取出一个个Json字符串
json_rdd=file_rdd.flatMap(lambda x:x.split("|"))
# 将一个个字符串转换为字典
dict_rdd=json_rdd.map(lambda x:json.loads(x))
# print(dict_rdd.collect())
# 取出城市和销售额数据
dict_rdd_select=dict_rdd.map(lambda x:(x["areaName"],int(x["money"])))
# 按照城市分组按销售额聚合
reduce_rdd=dict_rdd_select.reduceByKey(lambda a,b:a+b)
# 按照销售额聚合结果进行排序
sort_rdd=reduce_rdd.sortBy(lambda x:x[1],ascending=False,numPartitions=1)
print(sort_rdd.collect())

category_dict_rdd=dict_rdd.map(lambda x:x["category"]).distinct()
print(category_dict_rdd.collect())

beijing_category_rdd=dict_rdd.filter(lambda x:x["areaName"]=="上海").map(lambda x:x["category"]).distinct()
print("结果如下：",beijing_category_rdd.collect())

sc.stop()