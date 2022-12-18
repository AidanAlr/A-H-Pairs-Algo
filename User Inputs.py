
import numpy as np
import pandas as pd
import yfinance as yf

pd.set_option('display.max_columns', None)

def main():
    stocks = stock_list()
    stock_df = extracted_data(stocks)
    highest_corr_pair(stock_df)


def stock_list():
    user_input = input('Enter your tickers separated by a "space" please.')
    stocks = list(user_input.upper().split())
    return stocks


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
    np.fill_diagonal(corr_matrix.values, np.nan)
    print(corr_matrix)
    print('''
    Correlation Pairs:''')
    corr_pairs = corr_matrix.unstack().drop_duplicates().sort_values(kind='quicksort')
    print(corr_pairs)

    # Find the index of the maximum value in the corr_pairs array
    max_corr_index = corr_pairs.idxmax()

    # Extract the ticker symbols of the two stocks from the max_corr_index
    ticker_1, ticker_2 = max_corr_index

    # Print the ticker symbols
    print(f'The assets with the highest correlation are {ticker_1} and {ticker_2}')

main()