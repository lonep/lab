from re import X
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


Davis = pd.read_csv('Davis.csv')

Davis.dropna(inplace=True);
Davis = Davis.drop(Davis[Davis.height < 100].index )
Davis = Davis.drop(Davis[Davis.height > 215].index )

Davis = Davis.drop(Davis[Davis.weight < 40].index )
Davis = Davis.drop(Davis[Davis.weight > 140].index )
#print(Davis)

train, test = train_test_split(Davis, test_size = 50)


fig, axes = plt.subplots(3,2)

axes[0][0].hist(train['height'], bins='auto', color = 'orange', label = 'height')
axes[0][1].hist(train['weight'], bins='auto', label = 'weight')

axes[1][0].hist(train[train['sex'] == 'M']['height'], bins='auto', label = 'Man height')
axes[1][1].hist(train[train['sex'] == 'M']['weight'], bins='auto', label = 'Man weight')

axes[2][0].hist(train[train['sex'] == 'F']['height'], bins='auto', color = 'pink', label = 'Female height')
axes[2][1].hist(train[train['sex'] == 'F']['weight'], bins='auto', color = 'pink', label = 'Female weight')

for i in range(3):
    for j in range(2):
        axes[i][j].legend()

train.replace({'M':0,'F':1}, inplace=True)
test.replace({'M':0,'F':1}, inplace=True)

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

for i in range(number):
    x1_min, x1_max = trainX[:,0].min() - 0.5, trainX[:,1].max()+0.5
    x2_min, x2_max = trainX[:,0].min() - 0.5, trainX[:,1].max()+0.5
    xx1,xx2 = np.mgrid[x1_min:x1_max:100j, x2_min:x2_max:100j]
    X_pred = np.column_stack([xx1.reshape(-1), xx2.reshape(-1)])
    y_pred = clf.predict(X_pred)
    axes1[i].scatter(trainX[prd == 0][:,1], trainX[prd == 0][:,0], color='orange', label='Man')
    axes1[i].scatter(trainX[prd == 1][:,1], trainX[prd == 1][:,0], color='blue', label='Female')
    axes1[i].pcolormesh(xx1, xx2, y_pred.reshape(xx1.shape), cmap=ListedColormap(['orange','blue']), alpha=0.45, shading='auto')
    axes1[i].set_ylabel('weight')
    axes1[i].set_xlabel('height')
    axes1[i].legend()
    
plt.show()

