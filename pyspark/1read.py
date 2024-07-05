
from pyspark.sql import SparkSession
import numpy as np
import datetime
# Create a SparkSession
s = datetime.datetime.now()
spark = SparkSession.builder.appName("ReadCSV").getOrCreate()

# Read a CSV file as a DataFrame
df = spark.read.csv("/home/tspl/Desktop/Python Test/Untitled 1.csv", header=True)
# df = spark.read.csv("path/to/csv/file.csv", header=True, inferSchema=True)

# Show the first few rows of the DataFrame
df.show()

from pyspark.ml.linalg import Vectors

# Create a SparkSession
spark = SparkSession.builder.appName("ModelToDF").getOrCreate()

# Create some sample model objects
model_data = [
    (1, Vectors.dense([0.5, 0.1, -0.2])),
    (2, Vectors.dense([-0.3, 0.2, 0.4])),
    (3, Vectors.dense([0.2, -0.4, -0.1]))
]

# Convert the model objects to a DataFrame
df = spark.createDataFrame(model_data, ["iiiiiiiid", "features"])

# Show the DataFrame
df.show()

print(datetime.datetime.now()-s)