import requests
import json
import pandas as pd
import time

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
            'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}


main_url = "https://www.nseindia.com/"
response = requests.get(main_url, headers=headers)
print(response.status_code)
cookies = response.cookies

url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
bank_nifty_oi_data = requests.get(url, headers=headers, cookies=cookies)
print(bank_nifty_oi_data.status_code)
# print("BN OI data", bank_nifty_oi_data.text)

data = json.loads(bank_nifty_oi_data.text)
df = pd.DataFrame(data)

def get_current_data():
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    bank_nifty_oi_data = requests.get(url, headers=headers, cookies=cookies)
    print(bank_nifty_oi_data.status_code)
    # print("BN OI data", bank_nifty_oi_data.text)

    data = json.loads(bank_nifty_oi_data.text)
    df = pd.DataFrame(data)
    return df

def last_expiry():
    return df['records']['expiryDates'][0]

# len = len(df['records']['data'])

def put_oi():
    put_sum = 0
    df2 = get_current_data()
    for i in range(0,len):
        if df2['records']['data'][i]['expiryDate'] == last_expiry:
            # if(df['records']['data'][i]['PE']['openInterest'] > 10000):
            # print(df['records']['data'][i]['PE']['openInterest'])
            # print(df['records']['data'][i]['strikePrice'])
            
            put_sum += df2['records']['data'][i]['PE']['openInterest']
            # print("----------------------------")
    return put_sum

def call_oi():
    call_sum = 0
    df2 = get_current_data()       
    for i in range(0,len):
        if df2['records']['data'][i]['expiryDate'] == last_expiry:
            # if(df['records']['data'][i]['PE']['openInterest'] > 10000):
            # print(df['records']['data'][i]['PE']['openInterest'])
            # print(df['records']['data'][i]['strikePrice'])
            
            call_sum += df2['records']['data'][i]['CE']['openInterest']
            # print("----------------------------")
    return call_sum


def change_in_put_oi():
    put_sum = 0
    df2 = get_current_data()
    for i in range(0,len):
        if df2['records']['data'][i]['expiryDate'] == last_expiry:
            # if(df['records']['data'][i]['PE']['openInterest'] > 10000):
            # print(df['records']['data'][i]['PE']['openInterest'])
            # print(df['records']['data'][i]['strikePrice'])
            
            put_sum += df2['records']['data'][i]['PE']['changeinOpenInterest']
            # print("----------------------------")
    return put_sum

def change_in_call_oi():
    call_sum = 0 
    df2 = get_current_data()      
    for i in range(0,len):
        if df2['records']['data'][i]['expiryDate'] == last_expiry:
            # if(df['records']['data'][i]['PE']['openInterest'] > 10000):
            # print(df['records']['data'][i]['PE']['openInterest'])
            # print(df['records']['data'][i]['strikePrice'])
            
            call_sum += df2['records']['data'][i]['CE']['changeinOpenInterest']
            # print("----------------------------")
    return call_sum


def current_pcr_value():
    return put_oi()/call_oi()


def change_in_oi_current_pcr_value():
    return change_in_put_oi()/change_in_call_oi()


# print(current_pcr_value())
# print("PUT SUM: ", put_oi())
# print("CALL SUM: ", call_oi())

# print("PCR Value: ", put_oi()/ call_oi())

def current_value():
    df2 = get_current_data()
    return df2['records']['data'][0]['PE']['underlyingValue']

def current_strike_price():
    return int((50 - current_value()%50) + current_value())
    


# print(current_strike_price())
def put_current_strike_price_value():
    df = get_current_data()

    length = len(df['records']['data'])
    
    # print(df['records']['data'][0]['PE']['strikePrice'])
    # print(length)
    current_strike = current_strike_price()
    last_expiry_date = last_expiry()
    # print(current_strike)
    # print(type(current_strike))
    for i in range(0,length):
        if df['records']['data'][i]['strikePrice'] == current_strike and df['records']['data'][i]['expiryDate'] == last_expiry_date:
            # print(df['records']['data'][i]['PE']['bidprice'])
            return df['records']['data'][i]['PE']['lastPrice']
        #     return "Error put_current_strike_price()"
        
def call_current_strike_price_value():
    df = get_current_data()

    length = len(df['records']['data'])
    
    # print(df['records']['data'][0]['PE']['strikePrice'])
    # print(length)
    current_strike = current_strike_price()
    last_expiry_date = last_expiry()
    # print(current_strike)
    # print(type(current_strike))
    for i in range(0,length):
        if df['records']['data'][i]['strikePrice'] == current_strike and df['records']['data'][i]['expiryDate'] == last_expiry_date:
            # print(df['records']['data'][i]['PE']['bidprice'])
            return df['records']['data'][i]['CE']['lastPrice']
        # else:
        #     return "Error call_current_strike_price()"
    

def call_value(strike_price):
    df = get_current_data()

    length = len(df['records']['data'])
    
    # print(df['records']['data'][0]['PE']['strikePrice'])
    # print(length)
    strike = strike_price
    last_expiry_date = last_expiry()
    # print(current_strike)
    # print(type(current_strike))
    for i in range(0,length):
        if df['records']['data'][i]['strikePrice'] == strike and df['records']['data'][i]['expiryDate'] == last_expiry_date:
            # print(df['records']['data'][i]['PE']['bidprice'])
            return df['records']['data'][i]['CE']['lastPrice']
 
 
def put_value(strike_price):
    df = get_current_data()

    length = len(df['records']['data'])
    
    # print(df['records']['data'][0]['PE']['strikePrice'])
    # print(length)
    strike = strike_price
    last_expiry_date = last_expiry()
    # print(current_strike)
    # print(type(current_strike))
    for i in range(0,length):
        if df['records']['data'][i]['strikePrice'] == strike and df['records']['data'][i]['expiryDate'] == last_expiry_date:
            # print(df['records']['data'][i]['PE']['bidprice'])
            return df['records']['data'][i]['PE']['lastPrice']   
        
        
# print(put_value(18900))
# print(call_value(18900))