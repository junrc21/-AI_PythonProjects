import math
import matplotlib.pyplot as plt 
import numpy as np 
from sklearn.neighbors import KNeighborsRegressor

input = np.genfromtxt('C:\AI Projects\AI_Datasets\machine.data', delimiter=',', usecols=(2, 3, 4, 5, 6, 7))
output = np.genfromtxt('C:\AI Projects\AI_Datasets\machine.data', delimiter=',', usecols=(8))

K = 3

x = input[:206]
y = output[:206]

knn = KNeighborsRegressor(n_neighbors=K)
result = knn.fit(x, y).predict(x)

result = result.round(decimals=1)

plt.plot(np.linspace(-1,1,206), y, label='expected', color='green')
plt.plot(np.linspace(-1,1,206), result, label='predicted', color='blue')
plt.legend()
plt.show()

#print('Predicted: %d' % knn.predict([x[13]]))
#print('Expected: %d ' % y[13])








