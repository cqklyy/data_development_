"""
演示RDD的flatmap成员的使用
"""

from pyspark import SparkContext,SparkConf
import os
os.environ['PYSPARK_PYTHON']="F:/anaconda/envs/Python37/python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.parallelize(["cqk love lyy","cqk","love","lyy"])

rdd2=rdd.map(lambda x:x.split(" "))
rdd3=rdd.flatMap(lambda x:x.split(" "))
print(rdd2.collect())
print(rdd3.collect())

sc.stop()