from re import X
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


df = pd.read_csv('Davis.csv')


df.drop('Unnamed: 0', axis=1, inplace=True)

#Убрали аномальные значения из выборки
df = df.drop(df[df.height < 100].index )
df = df.drop(df[df.height > 215].index )

df = df.drop(df[df.weight < 40].index )
df = df.drop(df[df.weight > 140].index )

print(df.head())
print(df.isna().sum())


train, test = train_test_split(df, test_size = 50)


fig, axes = plt.subplots(3,2)

axes[0][0].hist(df['height'], bins='auto', color = 'orange', label = 'height')
axes[0][1].hist(df['weight'], bins='auto', label = 'weight')

axes[1][0].hist(df[df['sex'] == 'M']['height'], bins='auto', label = 'Man height')
axes[1][1].hist(df[df['sex'] == 'M']['weight'], bins='auto', label = 'Man weight')

axes[2][0].hist(df[df['sex'] == 'F']['height'], bins='auto', color = 'pink', label = 'Female height')
axes[2][1].hist(df[df['sex'] == 'F']['weight'], bins='auto', color = 'pink', label = 'Female weight')


for i in range(3):
    for j in range(2):
        axes[i][j].legend()

train.replace({'M':0,'F':1}, inplace=True)
test.replace({'M':0,'F':1}, inplace=True)

print(test.head())
print(train.head())

trainX = train.loc[:,'weight':'height'].to_numpy()
trainY = train['sex'].to_numpy()
clf = LogisticRegression().fit(trainX,trainY)
print('Score: ',clf.score(trainX, trainY))

testX = test.loc[:,'weight':'height'].to_numpy()
testY = test['sex'].to_numpy()
prd = clf.predict(testX)
print('Accuracy score: ',accuracy_score(prd,testY))

prd = clf.predict(trainX)

number = 2
fig1, axes1 = plt.subplots(number)

axes1[0].set_title('Тренировочная выборка')
axes1[1].set_title('Тестовая выборка')

x1_min, x1_max = trainX[:,0].min() - 0.5, trainX[:,0].max()+0.5
x2_min, x2_max = trainX[:,1].min() - 0.5, trainX[:,1].max()+0.5

meshgrid = 0.5

xx1,xx2 = np.meshgrid(np.arange(x1_min, x1_max, h), np.arange(x2_min, x2_max, h))
Z = clf.predict(np.c_[xx1.ravel(), xx2.ravel()])


Z = Z.reshape(xx1.shape)
axes1[0].pcolormesh(xx1, xx2, Z, cmap=ListedColormap(['orange','blue']),shading="auto", alpha=0.3)

axes1[0].scatter(trainX[prd == 0][:,0], trainX[prd == 0][:,1], color='orange', label='M')
axes1[0].scatter(trainX[prd == 1][:,0], trainX[prd == 1][:,1], color='blue', label='F')
axes1[0].set_ylabel('weight')
axes1[0].set_xlabel('height')
axes1[0].legend()

x1_min, x1_max = testX[:,0].min() - 0.5, testX[:,0].max()+0.5
x2_min, x2_max = testX[:,1].min() - 0.5, testX[:,1].max()+0.5

xx1,xx2 = np.meshgrid(np.arange(x1_min, x1_max,h), np.arange(x2_min, x2_max, h))
Z = clf.predict(np.c_[xx1.ravel(), xx2.ravel()])

Z = Z.reshape(xx1.shape)
pred = clf.predict(testX)

axes1[1].pcolormesh(xx1, xx2, Z, cmap=ListedColormap(['orange','blue']),shading="auto", alpha=0.3)
axes1[1].scatter(testX[pred == 0][:,0], testX[pred == 0][:,1], color='orange', label='M')
axes1[1].scatter(testX[pred == 1][:,0], testX[pred == 1][:,1], color='blue', label='F')
axes1[1].set_ylabel('weight')
axes1[1].set_xlabel('height')
axes1[1].legend()



    
plt.show()

