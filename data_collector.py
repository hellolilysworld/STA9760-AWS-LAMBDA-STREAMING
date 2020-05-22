import json
import boto3
import os
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')
import yfinance as yf

def lambda_handler(event, context):
    lstsym = ['FB','SHOP','BYND','NFLX','PINS','SQ','TTD','OKTA','SNAP','DDOG']

    data = yf.download(
            tickers = ' '.join(lstsym),
            start = '2020-05-15',
            end = '2020-05-16',
            period = "1d",
            interval = "1m",
            group_by = 'ticker',
            auto_adjust = True,
            threads = True,
        )
    res = []
    for sym in lstsym:
        for i,r in data[sym].iterrows():
            res += [{'high':r['High'],'low':r['Low']
                  ,'ts':i.strftime('%Y-%m-%d %H:%M:%S'),'name':sym}]
    
    # initialize boto3 client
    fh = boto3.client("firehose", "us-east-1")
    as_jsonstr = json.dumps(res)
    
    for row in res:
        # convert it to JSON -- IMPORTANT!!
        as_jsonstr_row = json.dumps(row)

        # this actually pushed to our firehose datastream
        # we must "encode" in order to convert it into the
        # bytes datatype as all of AWS libs operate over
        # bytes not strings
        fh.put_record(
            DeliveryStreamName="project-3-firehose", 
            Record={"Data": as_jsonstr_row.encode('utf-8')})

    # return
    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Recorded: {as_jsonstr}')
    }