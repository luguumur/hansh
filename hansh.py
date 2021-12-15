import requests
from bs4 import BeautifulSoup

#TDBM
main_url = "https://www.tdbm.mn/mn/exchange"
respose = requests.get(main_url)
soup = BeautifulSoup(respose.text.encode("utf-8"), "html.parser")
div = soup.find("div", id = "exchange-table-result")
table = div.find("table")

headers = ['flag', 'name', 'mongol_bank', 'belen_bus_avah', 'belen_bus_zarah', 'belen_avah', 'belen_zarah']
table_rows = [ row for row in table.find_all('tr')]

result = [{headers[index]:cell.text.replace("\n", "").replace(" ","") for index,cell in enumerate(row.find_all("td")) } for row in table_rows]

for i in result:  
    if 'name' in i:
        if i['name'] == 'АНУ-ындоллар': 
            print("TDBM")
            print(i)


#KHANBANK
khan_main_url = "https://www.khanbank.com/mn/home/ratesForSites/"
khan_respose = requests.get(khan_main_url)
khan_soup = BeautifulSoup(khan_respose.text.encode("utf-8"), "html.parser")
khan_table = khan_soup.find("table")

headers = ['flag', 'belen_avah', 'belen_zarah', 'belen_bus_avah', 'belen_bus_zarah']
table_rows = [ row for row in khan_table.find_all('tr')]

result = [{headers[index]:cell.text.replace("\n", "").replace(" ","").replace("\xa0","")  for index,cell in enumerate(row.find_all("td")) } for row in table_rows]

for i in result:  
    if 'flag' in i:
        if i['flag'] == 'USD':
            print("Khanbank")
            print(i)
