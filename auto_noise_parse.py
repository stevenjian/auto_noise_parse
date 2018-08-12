import pandas as pd
import collections as co
from bs4 import BeautifulSoup
import requests
html_string ='''

  '''
url = 'http://www.auto-decibel-db.com/index_kmh.html'
html = requests.get(url).text
#soup = BeautifulSoup(html_string, 'lxml')  # Parse the HTML as a string
soup = BeautifulSoup(html, "lxml")
#table = soup.find_all('table')[0]  # Grab the first table
table = soup.find('table', id="resultTable")
table_body = table.find('tbody')
table_head = table.find('thead')
header = []
for th in table_head.findAll('th'):
    key = th.get_text()
    header.append(key)
endrows = 0

#for tr in table.findAll('tr'):
#    if tr.findAll('th')[0].get_text() in (''):
#        endrows += 1

rows = len(table.findAll('tr'))

list_of_dicts = []
for row in range(rows):
    the_row = []
    try:
        table_row = table.findAll('tr')[row]
        for tr in table_row:
            value = tr.get_text()
            the_row.append(value)
        od = co.OrderedDict(zip(header,the_row))
        list_of_dicts.append(od)
    except AttributeError:
        continue

df = pd.DataFrame(list_of_dicts)
print(df)

