from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("Consumer Trends Pulse") \
    .getOrCreate()

# Load your television data (assume it's in CSV format)
tv_data = spark.read.csv("path/to/television_data.csv", header=True, inferSchema=True)

# Data processing to find the top 5 products
top_products = tv_data \
    .groupBy("product_name") \
    .agg({"market_demand_period": "count"}) \
    .withColumnRenamed("count(market_demand_period)", "popularity") \
    .orderBy(col("popularity").desc()) \
    .limit(5)

# Collect results
results = top_products.collect()

# Save the results to a file or return them for Streamlit
with open("top_tv_products.txt", "w") as f:
    for row in results:
        f.write(f"{row['product_name']}: {row['popularity']}\n")

spark.stop()
