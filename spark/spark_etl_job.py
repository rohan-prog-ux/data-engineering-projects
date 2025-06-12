from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETL Job").getOrCreate()
df = spark.read.csv("data.csv", header=True)
df = df.dropna()
df.write.parquet("cleaned_data.parquet")
