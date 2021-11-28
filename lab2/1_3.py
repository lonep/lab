import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

housing = pd.read_csv('housing.csv')

t_validation, test = train_test_split(housing, test_size=0.2)
train, validation = train_test_split(t_validation, test_size=0.2)

df_dummy = pd.get_dummies(train, columns=['ocean_proximity'])
#print(df_dummy)

housing['total_rooms'] /= housing['households']
housing['total_bedrooms'] /= housing['households']

housing.rename(columns={'total_rooms':'average_rooms', 'total_bedrooms':'average_bedrooms'}, inplace=True)

count_value = housing.isna().sum()
print(count_value)

housing['average_bedrooms'].fillna(value=housing['average_bedrooms'].mean(), inplace=True)

count_value = housing.isna().sum()
print(count_value)

scaler = StandardScaler()

print('iloc:')
print(housing.iloc[:,0:2])

housing.iloc[:,0:2] = scaler.fit_transform(housing.iloc[:,0:2].to_numpy())
print(housing)
