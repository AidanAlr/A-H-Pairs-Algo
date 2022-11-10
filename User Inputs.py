import numpy
import numpy as np
import pandas as pd
import math
import time
import datetime
import os
import glob
import yfinance as yf

def stock_list():
    user_input = input('Enter your tickers separated by a "space" please.')
    stock_l = list(user_input.upper().split())
    return stock_l

def extract_data():
    ticker_string = ''
    for tickers in stock_list():
        ticker_string += tickers + ' '

    ticker_string = ticker_string.strip()
    print(yf.download(f'{ticker_string}', start='2015-01-01', end='2020-01-01'))

extract_data()