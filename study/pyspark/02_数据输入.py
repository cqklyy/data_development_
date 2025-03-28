"""
演示通过PySpark代码加载数据，即数据输入
"""
from pyspark import SparkContext,SparkConf

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

# RDD:分布式弹性数据集，是PySpark中数据计算的载体

# # 通过parallelize方法将Python对象加载到Spark内，成为RDD对象
# rdd1=sc.parallelize([1,2,3,4,5])
# rdd2=sc.parallelize((1,2,3,4,5))
# rdd3=sc.parallelize("1,2,3,4,5")
# rdd4=sc.parallelize({1,2,3,4,5})
#
# # 如果要查看RDD里面有什么内容，需要看collect()方法
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())

# 用textFile方法，读取文件数据加载到Spark内，成为RDD对象
rdd=sc.textFile("F:/pythonProject/data_development/data_input/hello.txt")
print(rdd.collect())

sc.stop()
