"""
演示RDD的map成员方法的使用
"""

from pyspark import SparkContext,SparkConf
import os
os.environ["PYSPARK_PYTHON"]="F:/anaconda/envs/Python37/python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("map_test")
sc=SparkContext(conf=conf)

rdd=sc.parallelize([1,2,3,4,5])

# def func(data):
#     return data*10

rdd2=rdd.map(lambda x:x*5).map(lambda x:x+5)

print(rdd2.collect())
# (T) -> U


sc.stop()
