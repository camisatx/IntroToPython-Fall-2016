from datetime import datetime
import pandas as pd


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


if __name__ == '__main__':

    test_ticker = 'AAPL'
    test_interval = 'd'
    test_start = datetime(2010, 1, 1)
    test_end = datetime.now()           # specified date or current date

    price_df = download_prices(ticker=test_ticker, start=test_start,
                               end=test_end, interval=test_interval)

    price_df.to_csv('%s_%s.csv' % (test_ticker, test_interval))
