import pandas as pd
import collections as co
from bs4 import BeautifulSoup
import requests
import os

url = 'http://www.auto-decibel-db.com/index_kmh.html'
html = requests.get(url).text

soup = BeautifulSoup(html, "lxml")

table = soup.find('table', id="resultTable")
table_body = table.find('tbody')
table_head = table.find('thead')
header = []
for th in table_head.findAll('th'):
    key = th.get_text()
    header.append(key)


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
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path+"\\"+"auto_noise.csv")
df.to_csv(dir_path+"\\"+"auto_noise.csv")

