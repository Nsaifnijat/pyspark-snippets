# -*- coding: utf-8 -*-

import pyspark
from pyspark.sql import SparkSession
#for using pyspark, create sparksession, we name it Practice
spark = SparkSession.builder.appName('Practice').getOrCreate()
df_spark = spark.read.csv('test1.csv')
print(df_spark)