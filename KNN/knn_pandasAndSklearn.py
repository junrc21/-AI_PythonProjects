import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

train_file = pd.read_csv('C:\AI Projects\AI_Datasets\shoes_train.csv', header=None)
test_file = pd.read_csv('C:\AI Projects\AI_Datasets\shoes_test.csv', header=None)

cols_output = pd['class']
cols_input = train_file['shoe size', 'height']

input_train = train_file.iloc[:, [0, 1]]
output_train = train_file.iloc[:,[2]]

input_test = test_file.iloc[:, [0, 1]]
output_test = test_file.iloc[:, [2]]

knn = KNeighborsClassifier(n_neighbors=3, weights='distance')
knn.fit(input_train, output_train)
labels = knn.predict(input_test)

print(knn.predict(input_test[0]))
print(output_test[0])

