# STA9760-AWS-LAMBDA-STREAMING

## [Analysis](Analysis.ipynb)

The analysis above was performed using a csv dataset output from an AWS Athena (prestodb) query (query.sql) run against data in an s3 bucket.  This data was collected using a lambda functon "data_collector.py" to use the yfinance library to feed data through a Kinesis fire house.  This fire hose then passed the data to a data transformer lambda to split the input into seperate rows before saving into s3.

## Data Collector configuration
API Gateway: https://uf2zvm5gkk.execute-api.us-east-1.amazonaws.com/default/DataCollector

![data_collector](/assets/lambda_config.PNG)

## Firehose monitoring
![firehose](/assets/firehose_monitor.PNG)
