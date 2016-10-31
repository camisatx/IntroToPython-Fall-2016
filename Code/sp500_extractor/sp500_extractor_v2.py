import csv
from lxml import html
import time
import requests

"""
Make it work, make it right, make it fast

Extract the tickers from the S&P 500 table on Wikipedia, process them into
a list and save them into a CSV file.
"""


def download_data(url):
    """ Download the HTML from the provided url.

    http://docs.python-requests.org/en/master/user/quickstart/

    :param url: String of the url
    :return: String of the raw HTML
    """

    raw_html = requests.get(url).content
    html_string = html.fromstring(raw_html)
    return html_string


def extract_table_tickers(raw_html):
    """ Extract the tickers from the table that is in the provided HTML string

    # HTML table structure
    http://www.w3schools.com/html/html_tables.asp

    # Python HTML scraping
    http://docs.python-guide.org/en/latest/scenarios/scrape/

    # HTML table parsing with xpath
    http://www.w3schools.com/xml/xpath_syntax.asp

    :param raw_html: String of the raw HTML
    :return: List of the tickers from the table
    """

    ticker_list = []

    # Pull first HTML table from HTML string, then loop through each HTML row
    for html_row in raw_html.xpath('//table[1]'):
        # Pull each HTML row's code that starts with a <tr> flag
        for col in html_row.xpath('.//tr'):
            # Create a list of text values from each column in this HTML row
            row_list = [item.text_content() for item in col.xpath('.//td')]
            # Only process table row lists that have values
            if row_list:
                # Tickers are in the first column of the row
                ticker = row_list[0].strip()
                # Append each row's ticker to the ticker list
                ticker_list.append(ticker)

    # Alphabetize ticker list
    ticker_list.sort()

    return ticker_list


def save_list_to_csv(ticker_list, csv_name):
    """ Save the provided list to a CSV file.

    http://gis.stackexchange.com/a/72476

    :param ticker_list: List of strings
    :param csv_name: String of the name to use for the CSV
    :return: Nothing
    """

    # Save the ticker list to a csv file
    with open(csv_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for ticker in ticker_list:
            writer.writerow([ticker])


if __name__ == '__main__':
    start_time = time.time()

    sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500_csv_output = 'sp500_tickers.csv'

    # Download and process the tickers out of the HTML
    sp500_html = download_data(url=sp500_url)
    sp500_ticker_list = extract_table_tickers(raw_html=sp500_html)
    print(sp500_ticker_list)

    # Save the ticker list to a CSV
    save_list_to_csv(ticker_list=sp500_ticker_list, csv_name=sp500_csv_output)

    end_time = time.time()
    run_time = round(end_time - start_time, 2)
    print('Finished extracting the S&P 500 ticker list in %s seconds' %
          run_time)
