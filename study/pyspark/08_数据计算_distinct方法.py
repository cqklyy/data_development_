"""
演示RDD的distinct成员方法的使用
"""

from pyspark import SparkContext,SparkConf
import os
os.environ['PYSPARK_PYTHON']="F:/anaconda/envs/Python37/python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.parallelize([1,1,2,3,3,6,6,6,9])
rdd2=rdd.distinct()
print(rdd2.collect())

sc.stop()