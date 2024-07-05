# import necessary modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# create a spark session
spark = SparkSession.builder.appName("Merge Dataframes").getOrCreate()

# create two dataframes
df1 = spark.createDataFrame([(1, "Alice"), (2, "Bob"), (3, "Charlie")], ["id", "name"])
df2 = spark.createDataFrame([(1, "USA"), (2, "Canada"), (3, "Mexico")], ["id", "country"])
df1.show()
print(df1,"------------------------")
# merge the dataframes using the id column
merged_df = df1.join(df2, col("df1.id") == col("df2.id"), "inner")

# show the merged dataframe
merged_df.show()
