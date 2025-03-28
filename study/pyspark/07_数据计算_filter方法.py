"""
演示RDD的filter成员方法的使用
"""

from pyspark import SparkContext,SparkConf
import os
os.environ['PYSPARK_PYTHON']="F:/anaconda/envs/Python37/python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.parallelize([1,2,3,4,5])
# 对RDD的数据进行过滤
rdd2=rdd.filter(lambda num:num%2==0)
print(rdd2.collect())


sc.stop()