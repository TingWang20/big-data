from pyspark.sql import SparkSession

# 创建 SparkSession 对象
spark = SparkSession.builder \
    .appName("PySpark Example") \
    .getOrCreate()

# 读取 CSV 文件
data_path = "path/to/your/data.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)

# 显示数据集的前几行
df.show()

# 执行一些数据转换操作
# 例如，过滤年龄大于等于 18 的行
filtered_df = df.filter(df["age"] >= 18)

# 对转换后的数据进行聚合操作
# 例如，按性别计算平均年龄
average_age_by_gender = filtered_df.groupBy("gender").avg("age")

# 显示聚合结果
average_age_by_gender.show()

# 将结果保存为 Parquet 文件
output_path = "path/to/save/output.parquet"
average_age_by_gender.write.parquet(output_path)

# 关闭 SparkSession
spark.stop()
