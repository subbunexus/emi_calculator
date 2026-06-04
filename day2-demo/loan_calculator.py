# Databricks notebook source
# Simple loan EMI calculator
from pyspark.sql.functions import col, lit, round as spark_round

spark.sql('USE CATALOG hdfc_pyspark')
spark.sql("CREATE DATABASE IF NOT EXISTS lab3")
spark.sql('DROP TABLE IF EXISTS hdfc_pyspark.lab3.day2_loan_demo')

data = [(1, 'Alice', 500000, 12, 36),
        (2, 'Bob', 300000, 15, 24),
        (3, 'Charlie', 1000000, 10, 60)]

df = spark.createDataFrame(data, ['id', 'name', 'amount', 'rate', 'tenure'])
df = df.withColumn('monthly_emi',
    spark_round(col('amount') * (col('rate')/1200) * (1 + col('rate')/1200)**col('tenure') / ((1 + col('rate')/1200)**col('tenure') - 1), 0))
df.write.mode('overwrite').saveAsTable('hdfc_pyspark.lab3.day2_loan_demo')
print('Loan EMI data created:')
display(df)