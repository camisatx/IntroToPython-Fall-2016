from bs4 import BeautifulSoup
import csv
import time
from urllib.request import urlopen

"""
Make it work, make it right, make it fast

Extract the tickers from the S&P 500 table on Wikipedia and process them into
a list. Then save the list into a CSV file.

# Python 3.5 retrieve URLs
https://docs.python.org/3/howto/urllib2.html#fetching-urls

# HTML tables
http://www.w3schools.com/html/html_tables.asp

# Install BeautifulSoup
http://stackoverflow.com/a/19957214
# Pip install with Python 3.5 Windows local install
C:\Users\<USERNAME>\AppData\Local\Programs\Python\Python35-32\Scripts\pip.exe install beautifulsoup4

# BS4 parsing
http://stackoverflow.com/a/23377804

# Save to CSV
http://gis.stackexchange.com/a/72476
"""

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

csv_output = 'sp500_tickers.csv'

start_time = time.time()

# Download the S&P 500 table from Wikipedia
with urlopen(url) as response:
    html = response.read()

# Let bs4 parse the table out of the html
soup = BeautifulSoup(html, 'lxml')
sp_500_table = soup('table')[0]

# print(sp_500_table)

# Process the downloaded object to get a list of tickers

ticker_list = []

# Cycle through every row of the table
for row in sp_500_table.findAll('tr'):
    # Only look through non-header rows
    if row.findAll('td'):
        # List of row data values
        cols = row.findAll('td')
        # Tickers are in first column; extract and strip text
        ticker = cols[0].text.strip()
        # Append row ticker to ticker list
        ticker_list.append(ticker)

# Alphabetize ticker list
ticker_list.sort()

# print(ticker_list)
# print(len(ticker_list))

# Save the ticker list to a csv file
with open(csv_output, 'w') as file:
    writer = csv.writer(file)
    for ticker in ticker_list:
        writer.writerow([ticker])

end_time = time.time()
run_time = round(end_time - start_time, 2)
print('Finished extracting S&P 500 ticker list in %s seconds' % run_time)
