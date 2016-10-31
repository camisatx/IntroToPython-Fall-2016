import csv
from lxml import html
import time
import requests

"""
Make it work, make it right, make it fast

Download and process the S&P 500 company data from Wikipedia into a dictionary
and save it into a CSV file.
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


def extract_table(raw_html):
    """ Extract the company data from the table that is in the HTML string.

    # HTML table structure
    http://www.w3schools.com/html/html_tables.asp

    # Python HTML scraping
    http://docs.python-guide.org/en/latest/scenarios/scrape/

    # HTML table parsing with xpath
    http://www.w3schools.com/xml/xpath_syntax.asp

    :param raw_html: String of the raw HTML
    :return: Dictionary of dictionaries with company data
    """

    company_info = {}

    # Pull first HTML table from HTML string, then loop through each HTML row
    for html_row in raw_html.xpath('//table[1]'):
        # Pull each HTML row's code that starts with a <tr> flag
        for col in html_row.xpath('.//tr'):
            # Create a list of text values from each column in this HTML row
            row_list = [item.text_content() for item in col.xpath('.//td')]
            # Only process table row lists that have values
            if row_list:
                # Extract each item based on which table column it is in
                ticker = row_list[0].strip()
                name = row_list[1].strip()
                sector = row_list[3].strip()
                industry = row_list[4].strip()
                headquarter = row_list[5].strip()

                # Save the company statistics in a dictionary that is saved
                #   to the company_info dictionary under the company's ticker
                company_info[ticker] = {'ticker': ticker,
                                        'name': name,
                                        'headquarter': headquarter,
                                        'sector': sector,
                                        'industry': industry}
    return company_info


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


def save_dict_to_csv(ticker_dict, csv_name):
    """ Save the provided dictionary to a CSV file.

    http://stackoverflow.com/a/10373268

    :param ticker_dict: Dictionary of the company statistics
    :param csv_name: String of the name to use for the CSV
    :return: Nothing
    """

    # Establish what the column headers should be
    headers = ['ticker', 'name', 'sector', 'industry', 'headquarter']

    # Save the ticker dictionary to a csv file
    with open(csv_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()

        # For each ticker in ticker_dict, add all the company data to the csv
        for ticker_data in ticker_dict.values():
            writer.writerow(ticker_data)


if __name__ == '__main__':
    start_time = time.time()

    sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500_csv_output = 'sp500_companies.csv'

    # Download and process the s&p 500 companies from the HTML table
    sp500_html = download_data(url=sp500_url)
    sp500_company_info = extract_table(raw_html=sp500_html)
    # print(sp500_company_info['AAPL'])

    # Save the company info to a CSV
    save_dict_to_csv(ticker_dict=sp500_company_info, csv_name=sp500_csv_output)

    end_time = time.time()
    run_time = round(end_time - start_time, 2)
    print('Finished extracting the S&P 500 ticker list in %s seconds' %
          run_time)
