from pyspark import SparkContext,SparkConf
import os
import json
os.environ['PYSPARK_PYTHON']="F:/anaconda/envs/Python37/python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.parallelize([1,2,3,4,5])

# collect算子，输出RDD为list对象
rdd_list:list=rdd.collect()
print(rdd_list)
print(type(rdd_list))

# reduce算子，对RDD1进行两两聚合
num=rdd.reduce(lambda a,b:a+b)
print(num)

# take算子，取出RDD前N个元素，组成list返回
take_list=rdd.take(3)
print(take_list)

# count算子，统计RDD内有多少条数据，返回值为数字
count_int=rdd.count()
print(count_int)


sc.stop()