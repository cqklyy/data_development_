from pyspark import SparkContext,SparkConf
import os
os.environ["PYSPARK_PYTHON"]="F:/anaconda/envs/Python37/python.exe"
os.environ["HADOOP_HOME"]="F:/software/hapdoop/hadoop-3.0.0/hadoop-3.0.0"
conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
# 第一种方法：全局将分区默认设置为1，可以将内容就写进一个文件当中
conf.set("spark.default.parallelism","1")
sc=SparkContext(conf=conf)
# 第二种方法：局部将分区默认设置为1，可以将内容就写进一个文件当中
rdd=sc.parallelize([1,2,3,4,5],numSlices=1)
rdd.saveAsTextFile("F:/pythonProject/data_development/data_input/Spark案例/RDD_output")


sc.stop()
