import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')

table = pd.merge(orders, products, how='inner', on='ProductID')
table['OrderSum'] = np.where((table['UnitPrice_x'] < table['UnitPrice_y']),table['Quantity']*table['QuantityPerUnit']*table['UnitPrice_x']*(1-table['Discount']),
                          table['Quantity']*table['QuantityPerUnit']*table['UnitPrice_y']*(1-table['Discount']))

print(table.groupby(by='CategoryName')['OrderSum'].mean())

table['Profit'] = table['OrderSum'] - table['Quantity']*table['UnitCost']*table['QuantityPerUnit']
print(table.head())

print('Категории товаров, обеспечивающие 80 процентов прибыли')

profit = table.groupby(by='CategoryName')['Profit'].sum()/table['Profit'].sum()

sum = 0
for i in range(len(profit)):
    sum += profit[i]
    if(sum <= 0.8):
        print(profit.index[i] + ' - обеспечивают ' + str(round(profit[i], 3)))
       
