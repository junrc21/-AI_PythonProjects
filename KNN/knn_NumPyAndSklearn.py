import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

input = np.genfromtxt('C:\AI Projects\AI_Datasets\movies.data', delimiter=',', usecols=(0, 1, 2, 3))
output = np.genfromtxt('C:\AI Projects\AI_Datasets\movies.data', delimiter=',', usecols=(4))

input_train, input_test, output_train, output_test = train_test_split(input, output, test_size=0.3, 
                                                                      random_state=42)



knn = KNeighborsClassifier(n_neighbors=15, p=2)
knn.fit(input_train, output_train)
labels = knn.predict(input_test)

hits = np.sum(labels == output_test)

print('total of train dataset: %d' % len(input_train))
print('Total of test dataset: %d' % len(input_test))
print('Total of hits: %d' % hits)
print('percentage of hits: %.2f%% ' % (100 * hits / (len(input_test)) )) 