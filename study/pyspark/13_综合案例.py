from pyspark import SparkContext,SparkConf
import os
os.environ["PYSPARK_PYTHON"]="F:/anaconda/envs/Python37/python.exe"
os.environ["HADOOP_HOME"]="F:/software/hapdoop/hadoop-3.0.0/hadoop-3.0.0"
conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
# 全局将分区默认设置为1，可以将内容就写进一个文件当中
conf.set("spark.default.parallelism","1")
sc=SparkContext(conf=conf)

# 读取文件转换为RDD
file_rdd=sc.textFile("F:/pythonProject/data_development/data_input/Spark案例/search_log.txt")
# TODO 需求1：热门搜索时间段TOP3(小时精度)
hour_top_rdd=file_rdd.map(lambda x:x.split("\t")).map(lambda x:x[0][:2]).map(lambda x:(x,1)).reduceByKey(lambda a,b:a+b)\
    .sortBy(lambda x:x[1],ascending=False,numPartitions=1).take(3)
print(hour_top_rdd)

# TODO 需求2：统计黑马程序员关键字在什么时候被搜索的最多
top_rdd=file_rdd.map(lambda x:x.split("\t")).filter(lambda x:x[2]=="黑马程序员").map(lambda x:(x[0][:2],1)).\
    reduceByKey(lambda a,b:a+b).sortBy(lambda x:x[1],ascending=False,numPartitions=1).take(1)
print(top_rdd)

# TODO 需求3：将数据转换为JSON格式，写出到文件中
file_rdd.map(lambda x:x.split("\t")).\
    map(lambda x:{"time":x[0],"use_id":x[1],"key_word":x[2],"rank1":x[3],"rank2":x[4],"url":x[5]}).\
    saveAsTextFile("F:/pythonProject/data_development/data_input/Spark案例/RDD_output")