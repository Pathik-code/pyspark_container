from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, desc
import pyspark
import sys
import os

def print_header():
    print("\n" + "="*50)
    print(" "*15 + "PySpark Environment Check")
    print("="*50 + "\n")

def print_version_info():
    print("\n" + "-"*20 + " System Information " + "-"*20)
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"PySpark Version: {pyspark.__version__}")
    print("-"*59 + "\n")

def create_spark_session():
    return SparkSession.builder \
        .appName("Organizations Analysis") \
        .master("spark://spark-master:7077") \
        .config("spark.ui.port", "4040") \
        .config("spark.driver.host", "localhost") \
        .config("spark.submit.deployMode", "client") \
        .config("spark.driver.bindAddress", "0.0.0.0") \
        .config("spark.driver.extraJavaOptions",
                "--add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED") \
        .config("spark.executor.extraJavaOptions",
                "--add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED") \
        .getOrCreate()

def analyze_data(spark):
    # Read CSV file
    df = spark.read.csv("/app/data/ShopBusinessCsv/organizations-1000.csv", header=True, inferSchema=True)

    # Show basic statistics
    print("\nDataset Overview:")
    print(f"Total Records: {df.count()}")
    print(f"Total Columns: {len(df.columns)}")

    # Show top industries
    print("\nTop 10 Industries by Company Count:")
    df.groupBy("Industry") \
        .agg(count("*").alias("count")) \
        .orderBy(desc("count")) \
        .show(10, False)

    # Show average employees by country
    print("\nTop 10 Countries by Average Number of Employees:")
    df.groupBy("Country") \
        .agg({"Number of employees": "avg"}) \
        .orderBy(desc("avg(Number of employees)")) \
        .show(10)

    return df

def main():
    try:
        print_header()
        print_version_info()

        print("Initializing Spark Session...")
        spark = create_spark_session()

        print("\nSpark Session successfully created!")
        print(f"Spark UI available at: {spark.sparkContext.uiWebUrl}")

        # Analyze the data
        df = analyze_data(spark)

        # Keep the session alive
        input("\nPress Enter to exit...")

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        try:
            spark.stop()
        except:
            pass

if __name__ == "__main__":
    main()
