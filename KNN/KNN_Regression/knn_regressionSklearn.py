from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt 
import numpy as np

#load sklearn dataset
boston = load_boston()

#set K value
K = 9 

#set only 50 elemts to x and y
x, y = boston.data[:50],  boston.target[:50]

#initialize KNeighborsRegressor passing K value
knn = KNeighborsRegressor(n_neighbors=K)

#fit data and predict
result = knn.fit(x, y).predict(x)

#plot expected and predicted for comparisson
plt.plot(np.linspace(-1,1,50), y, label='expected', color='green')
plt.plot(np.linspace(-1,1,50), result, label='predicted', color='blue')
plt.legend()
plt.show()


#print(boston.target[0])
#print(knn.predict([boston.data[0]]))

#y_ = knn.fit(boston.data, boston.target).predict([boston.data[12]])
#print(y_)
#print(boston.target[12])


