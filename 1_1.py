import json, csv

with open('sales.json') as file:
    json = json.load(file)
    
csv = csv.writer(open("sales3.csv", "w",encoding='utf8',newline=''))

csv.writerow(['item','country','year','sales'])
for item in json:
    for country in item["sales_by_country"]:
        for year in item["sales_by_country"][country].items():
            csv.writerow([item["item"],country, year[0], year[1]])
#csv.writerow(["aaaaaa","bbbbbb", "CCCCC", "KKKK"])
