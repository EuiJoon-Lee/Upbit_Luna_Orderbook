import requests
import json
import csv
from time import sleep
import datetime


idx = 0
while True:
    sorted_save_ask_bid = [None for _ in range(29)]
    order = []
    ask = []
    bid = []
    n = 0
    save_ask_bid = []
    Current_BTC_price = []
    a = 0
    i = 14
    j = 15
    t = []
    t1 = []
    t2 = []
    t = str(datetime.datetime.now()).split(' ')
    t1 = t[0]
    t2 = t[1].replace(':', '_',2)
    url = "https://api.upbit.com/v1/trades/ticks"

    querystring = {"market":"KRW-BTC"}
    response = requests.request("GET", url, params=querystring)
    BTC_KRW = response.json()
    BTC_price = BTC_KRW[0]
    Current_BTC_price = BTC_price["trade_price"]

    url = "https://api.upbit.com/v1/orderbook"
    querystring = {"markets":"BTC-LUNA"}
    response = requests.request("GET", url, params=querystring)
    BTC_LUNA = response.json()
    LUNA_orderbook = BTC_LUNA[0]
    ask_bid = LUNA_orderbook['orderbook_units']

    while n < 15:
        ask = []
        bid = []
        order = []
        orders = ask_bid[n]
        keys = ['ask_price', 'bid_price', 'ask_size', 'bid_size']
        n+=1
        for values in keys:
            if not keys: break
            order.append(orders[values])

        ask = []
        bid = []
        try:
            a += 1
            ask.append(order[0]*Current_BTC_price)
            ask.append(order[2])
            bid.append(order[1]*Current_BTC_price)
            bid.append(order[3])
            print(bid)
            sorted_save_ask_bid[i]=ask
            sorted_save_ask_bid[j]=bid                
            i -= 1
            j += 1
        except:
            print()
    with open(str(t1) + '_' + str(t2) + '_' + str(idx) + '.csv', "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(sorted_save_ask_bid)
    print('Saved!')
    idx+=1
    sleep(60)
