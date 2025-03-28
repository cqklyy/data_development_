"""
演示RDD的reduceByKey成员方法的使用
"""

from pyspark import SparkContext,SparkConf
import os
os.environ['PYSPARK_PYTHON']="F:/anaconda/envs/Python37/python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.parallelize([("cqk",99),("cqk",99),("lyy",99),("lyy",66)])
rdd2=rdd.reduceByKey(lambda a,b:a+b)

print(rdd2.collect())

sc.stop()