# KNN Implementation Algorithm with sklearn

#This Algorithm is used could be for a movie recomandation for example
#if Netflix wants recommend a film for you basesed in what you've been watched
#it could use KNN Algorithm, we just need the values from all movies (or N movies) that you've watched
#and calculate wich movie woul be more intersting (is Neighbor of) your recent movies

from sklearn.neighbors import KNeighborsClassifier

#create 2 arrays
input, output = [], []

#load data from file
with open('C:\AI Projects\AI_Datasets\movies.data', 'r') as file:
    for line in file.readlines():
        atrb = line.replace('\n', '').split(',')
        input.append([float(atrb[0]), float(atrb[1]), float(atrb[2]), float(atrb[3])])
        output.append(float(atrb[4]))

#set the percentage of data for training
percentage_train = 0.6 
limit = int (percentage_train * len(input))

#initialize KNeighborsRegressor passing K value
knn = KNeighborsClassifier(n_neighbors=15)

#fit data and predict at the limit
knn.fit(input[:limit], output[:limit])
labels = knn.predict(input[:limit])

hits, label_index = 0, 0

#calcule hits
for i in range(limit, len(input)):
    if labels[label_index] == output[i]:
        hits += 1
    label_index += 1

#print info
print('total of train dataset: %d' % limit)
print('Total of test dataset: %d' % int (len(input) - limit))
print('Total of hits: %d' % hits)
print('percentage of hits: %.2f%% ' % (100 * hits / (len(input) - limit) )) 


    


