from datetime import datetime
import pandas as pd
from matplotlib import pyplot as plt


def download_prices(ticker, start, end, interval='d'):
    """ Download the historical price data from Yahoo Finance for the provided
    ticker over the date range.

    https://stackoverflow.com/questions/35815269/python-requests-text-to-pandas-dataframe

    http://chart.finance.yahoo.com/table.csv?s=AAPL&a=00&b=1&c=2010&d=10&e=30&f=2016&g=d&ignore=.csv

    :param ticker: String of ticker
    :param start: Datetime object of the start date
    :param end: Datetime object of the end date
    :param interval: Optional string for the price history interval (d, w, m, v)
    :return: DataFrame of the raw stock prices
    """

    # Prepare the URL API component strings
    url_root = 'http://chart.finance.yahoo.com/table.csv?'
    url_ticker = 's=%s' % ticker
    url_interval = 'g=%s' % interval
    url_start = ('a=%s&b=%s&c=%s' % ((start.month - 1), start.day, start.year))
    url_end = ('d=%s&e=%s&f=%s' % ((end.month - 1), end.day, end.year))
    url_csv = 'ignore=.csv'

    # Final URL string for this ticker over the date range
    final_url = (url_root + url_ticker + '&' + url_start + '&' + url_end +
                 '&' + url_interval + '&' + url_csv)

    # Let pandas download the CSV file and convert it into a DataFrame
    raw_df = pd.read_csv(final_url, index_col=False)

    # Move the Date column to the DataFrame index
    raw_df.set_index(keys='Date', inplace=True)
    return raw_df


def sma(df, period):
    """ A simple moving average (SMA) is formed by computing the average price
    of a security over a specific number of periods.

    http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.rolling_mean.html

    :param df: DataFrame of the raw prices
    :param period: Integer of the periods to average
    :return: Series of the rolling average values
    """

    cur_price = df['Adj Close']
    roll_ma = pd.rolling_mean(cur_price, period)
    return roll_ma


if __name__ == '__main__':

    test_ticker = 'AAPL'
    test_interval = 'd'
    test_start = datetime(2010, 1, 1)
    test_end = datetime.now()           # specified date or current date

    price_df = download_prices(ticker=test_ticker, start=test_start,
                               end=test_end, interval=test_interval)

    # Remove all columns that we do not need
    price_df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis=1,
                  inplace=True)

    # Sort the prices oldest to newest (ascending)
    price_df.sort_index(axis=0, ascending=True, inplace=True)

    # Calculate the 50 period simple moving average
    sma_50 = sma(df=price_df, period=50)
    price_df['sma_%s' % 50] = sma_50

    # Calculate the 200 period simple moving average
    sma_200 = sma(df=price_df, period=200)
    price_df['sma_%s' % 200] = sma_200

    # Plot all the DataFrame columns
    # http://pandas.pydata.org/pandas-docs/version/0.18.1/visualization.html
    price_df.plot(title='%s_%s' % (test_ticker, test_interval))
    plt.show()

    price_df.to_csv('%s_%s.csv' % (test_ticker, test_interval))
