import requests as req
from xml.etree import ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
r = req.get('http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/01/2021&date_req2=24/11/2021&VAL_NM_RQ=R01235')

tree = ET.fromstring(r.text)



date_values = []
Dates = tree.findall('Record')
dollars_values = []
euro_values = []
yen_values = []
grivna = []
i = 0
for  child in tree:
    date_values.append(dt.datetime.strptime(child.attrib['Date'], "%d.%m.%Y").date())
    dollars_values.append(float(tree[i][1].text.replace(',','.')))
    i += 1

r = req.get('http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/01/2021&date_req2=24/11/2021&VAL_NM_RQ=R01239')
tree = ET.fromstring(r.text)
i = 0
for  child in tree:
    euro_values.append(float(tree[i][1].text.replace(',','.')))
    i += 1

r = req.get('http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/01/2021&date_req2=24/11/2021&VAL_NM_RQ=R01820')
tree = ET.fromstring(r.text)
i = 0
for  child in tree:
    yen_values.append(float(tree[i][1].text.replace(',','.')))
    i += 1

r = req.get('http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/01/2021&date_req2=24/11/2021&VAL_NM_RQ=R01720')
tree = ET.fromstring(r.text)
i = 0
for  child in tree:
    grivna.append(float(tree[i][1].text.replace(',','.')))
    i += 1        

fig, ax = plt.subplots()
ax.plot(date_values, dollars_values, label = "USD")
ax.plot(date_values, euro_values, label = "EUR")
ax.plot(date_values, yen_values, label = "YEN")
ax.plot(date_values, grivna, label = "UAH")
ax.set_xlabel('Date')
ax.set_ylabel('RUB')
ax.legend()
plt.show()


