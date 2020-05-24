# KNN Implementation Algorithm with sklearn

#This Algorithm is used could be for a movie recomandation for example
#if Netflix wants recommend a film for you basesed in what you've been watched
#it could use KNN Algorithm, we just need the values from all movies (or N movies) that you've watched
#and calculate wich movie woul be more intersting (is Neighbor of) your recent movies

from sklearn.neighbors import KNeighborsClassifier

input, output = [], []


with open('C:\AI course\Datasets\movies.data', 'r') as file:
    for line in file.readlines():
        atrb = line.replace('\n', '').split(',')
        input.append([float(atrb[0]), float(atrb[1]), float(atrb[2]), float(atrb[3])])
        output.append(float(atrb[4]))

percentage_train = 0.6 #percentage of data for training
limit = int (percentage_train * len(input))

knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(input[:limit], output[:limit])
labels = knn.predict(input[:limit])

hits, label_index = 0, 0

for i in range(limit, len(input)):
    if labels[label_index] == output[i]:
        hits += 1
    label_index += 1
    
print('total of train dataset: %d' % limit)
print('Total of test dataset: %d' % int (len(input) - limit))
print('Total of hits: %d' % hits)
print('percentage of hits: %.2f%% ' % (100 * hits / (len(input) - limit) )) 


    


