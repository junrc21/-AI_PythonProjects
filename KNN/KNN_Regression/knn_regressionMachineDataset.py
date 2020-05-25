import math
import matplotlib.pyplot as plt 
import numpy as np 
from sklearn.neighbors import KNeighborsRegressor

input = np.genfromtxt('C:\AI Projects\AI_Datasets\machine.data', delimiter=',', usecols=(2, 3, 4, 5, 6, 7))
output = np.genfromtxt('C:\AI Projects\AI_Datasets\machine.data', delimiter=',', usecols=(8))

#set K value
K = 3

#set the number of elements to get from file array
x = input[:206]
y = output[:206]

#create KNeighborsRegressor passing K value
knn = KNeighborsRegressor(n_neighbors=K)

#fit dataset and predict
result = knn.fit(x, y).predict(x)

#normalize to be 1 decimal
result = result.round(decimals=1)

#plot expected and predicted for comparisson
plt.plot(np.linspace(-1,1,206), y, label='expected', color='green')
plt.plot(np.linspace(-1,1,206), result, label='predicted', color='blue')
plt.legend()
plt.show()

#print('Predicted: %d' % knn.predict([x[13]]))
#print('Expected: %d ' % y[13])








