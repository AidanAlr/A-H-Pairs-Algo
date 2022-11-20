import numpy
import numpy as np
import pandas as pd
import math
import time
import datetime
import os
import glob
import yfinance as yf

pd.set_option('display.max_columns', None)

# 'main' function - used to run subsequent functions in sequence
def main():
    stocks = stock_list()
    stock_df = extracted_data(stocks)
    highest_corr_pair(stock_df)


# 'stock_list' function – requests ticker input from user, returns list with upper case, split tickers
def stock_list():
    user_input = input('Enter your tickers separated by a "space" please > ')
    stocks = list(user_input.upper().split())
    return stocks

# extracted_data function - adding tickers to a string, truncating the new string, 
# downloading and printing 5y historic closing data for the tickers
def extracted_data(stocks):
    ticker_string = ''
    for tickers in stocks:
        ticker_string += tickers + ' '
    ticker_string = ticker_string.strip()

    stock_df = yf.download(f'{ticker_string}', start='2015-01-01', end='2020-01-01')['Adj Close']

    print('Your generated stock data: ')
    print(stock_df)
    return stock_df


def highest_corr_pair(stock_df):
    print('Correlation Matrix generated from your stock picks: ')
    corr_matrix = stock_df.corr()
    print(corr_matrix)
    print('''
    Correlation Pairs:''')
    corr_pairs = corr_matrix.unstack().drop_duplicates().sort_values(kind='quicksort')
    np.fill_diagonal(corr_matrix.values, np.nan)
    print(corr_pairs)
    # np.fill_diagonal(corr_matrix.values, np.nan)
    # print(corr_matrix)
    # print('\n')


main()