import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')

table = pd.merge(orders, products, how='inner', on='ProductID')

print(products.groupby(by='CategoryName')['ProductName'].count())
print(products[products['CategoryName'] == 'Морепродукты'])

table.index = pd.to_datetime(orders['OrderDate'])
table.groupby(by=[table.index.month, table.index.year])['Quantity'].count().plot()
plt.title('Кол-во заказов по месяцам')
plt.ylabel('Заказы')
plt.xlabel('Месяц/Год')

table['OrderSum'] = np.where((table['UnitPrice_x'] < table['UnitPrice_y']),table['Quantity']*table['QuantityPerUnit']*table['UnitPrice_x']*(1-table['Discount']),
                          table['Quantity']*table['QuantityPerUnit']*table['UnitPrice_y']*(1-table['Discount']))

table.groupby(by='OrderID')
table.sort_values(by='OrderSum', ascending=False, inplace=True)
print('Cамые дорогие заказы')
print(table.head())
      
print('Продукты с максимальной стоимостью')
table.sort_values(by="UnitCost")
print(table.groupby(by='ProductName')['UnitCost'].max())


plt.show()
