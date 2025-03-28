from pyspark import SparkContext,SparkConf
import os
os.environ['PYSPARK_PYTHON']="F:/anaconda/envs/Python37/python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.textFile("F:/pythonProject/data_development/data_input/hello.txt")
word_rdd=rdd.flatMap(lambda x:x.split(" "))
# print(word_edd.collect())
# 将每个单词都转变成二元元组，单词为Key，value设置为1
word_with_one_rdd=word_rdd.map(lambda word:(word,1))
# print(word_with_one_rdd.collect())

result_rdd=word_with_one_rdd.reduceByKey(lambda a,b:a+b)
print(result_rdd.collect())

sc.stop()
