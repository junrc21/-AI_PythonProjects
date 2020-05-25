import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#load data from file setting the columns
input = np.genfromtxt('C:\AI Projects\AI_Datasets\movies.data', delimiter=',', usecols=(0, 1, 2, 3))
output = np.genfromtxt('C:\AI Projects\AI_Datasets\movies.data', delimiter=',', usecols=(4))

#Split the dataset:  test_size = 0.3 means 30% from data will be used to test
#the parametrs below need to be like this: x_train, x_test, y_train and y_test to get the data correctly
input_train, input_test, output_train, output_test = train_test_split(input, output, test_size=0.3, 
                                                                      random_state=42)


#create a KNeighborsClassifier setting 15 as neighbors to check and p=2 for euclidean distance 
knn = KNeighborsClassifier(n_neighbors=15, p=2)

#fit all data and start prediction
knn.fit(input_train, output_train)
labels = knn.predict(input_test)

#get the sum of hits
hits = np.sum(labels == output_test)

#print info
print('total of train dataset: %d' % len(input_train))
print('Total of test dataset: %d' % len(input_test))
print('Total of hits: %d' % hits)
print('percentage of hits: %.2f%% ' % (100 * hits / (len(input_test)) )) 