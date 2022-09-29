import requests 
from datetime import datetime
import time 
import string

ticker    =  input("Enter the ticker symbol: ").upper()
from_date =  input("Enter date in yyyy/mm/dd format: ")
to_date   =  input("Enter end date in yyyy/mm/dd format: ")
interval =   input("Enter interval in 1d, 1h, 1m, 1y format: ")

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')    
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')   

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

def get_url():
    url = f"https://query1.finance.yahoo.com/v7/finance/download/\
{ticker}?\
period1={from_epoch}\
&period2={to_epoch}\
&interval={interval}\
&events=history&includeAdjustedClose=true"
    # print(url)
    return url

headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
        (KHTML,like Gecko) Chrome/88.0.4324.96 Safari/537.36" }

content = requests.get(get_url(), headers=headers).content 

with open(f"{ticker}.csv", 'wb') as file:
    file.write(content)