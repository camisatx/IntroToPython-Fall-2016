import csv
from lxml import html
import time
import requests

"""
Make it work, make it right, make it fast

Extract the tickers from the S&P 500 table on Wikipedia, process them into
a list and save them into a CSV file.

# Retrieve HTML from URL with requests
http://docs.python-requests.org/en/master/user/quickstart/

# HTML table structure
http://www.w3schools.com/html/html_tables.asp

# Python HTML scraping
http://docs.python-guide.org/en/latest/scenarios/scrape/

# HTML table parsing with xpath
http://www.w3schools.com/xml/xpath_syntax.asp

# Save to CSV
http://gis.stackexchange.com/a/72476
"""

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

csv_output = 'sp500_tickers.csv'

start_time = time.time()

# Download the S&P 500 table from Wikipedia, creating a string of the raw HTML
raw_html = requests.get(url).content
html_string = html.fromstring(raw_html)

ticker_list = []

# Pull first HTML table out of the HTML string, then loop through each HTML row
for html_row in html_string.xpath('//table[1]'):
    # Pull each HTML row's code that starts with a <tr> flag
    for col in html_row.xpath('.//tr'):
        # Create a list of text values from each column in this HTML row
        table_row_list = [item.text_content() for item in col.xpath('.//td')]
        # Only process table row lists that have values
        if table_row_list:
            # Tickers are in the first column in the row (first list element)
            ticker = table_row_list[0].strip()
            # Append each row's ticker to the ticker list
            ticker_list.append(ticker)

# Alphabetize ticker list
ticker_list.sort()

print(ticker_list)

# Save the ticker list to a csv file
with open(csv_output, 'w', newline='') as file:
    writer = csv.writer(file)
    for ticker in ticker_list:
        writer.writerow([ticker])

end_time = time.time()
run_time = round(end_time - start_time, 2)
print('Finished extracting the S&P 500 ticker list in %s seconds' % run_time)
