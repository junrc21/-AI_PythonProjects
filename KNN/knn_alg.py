# KNN Implementation Algorithm
#This Algorithm is used could be for a movie recomandation for example
#if Netflix wants recommend a film for you basesed in what you've been watched
#it could use KNN Algorithm, we just need the values from all movies (or N movies) that you've watched
#and calculate wich movie woul be more intersting (is Neighbor of) your recent movies


import math

#Dataset of movies and their indices values:
#Colum_1:  Violence
#Colum_2:  Romance
#Colum_3:  Action
#Colum_4:  Comedy'
dataset = []

#Open file for read
with open('C:\AI Projects\AI_Datasets\movies.data', 'r') as file:
    for line in file.readlines():
        atrb = line.replace('\n', '').split(',')
        dataset.append([float(atrb[0]), float(atrb[1]), float(atrb[2]), float(atrb[3]), float(atrb[4])])


#Calc euclidean_distance
def euclidean_dist(values1, values2):
    dim, sum = len(values1), 0
    
    #for each value of datasets (train and test) we need to calculate the euclidean_distance    
    for i in range(dim - 1):
        
        #Sub the 2 values and raise to 2
        #then, add it to Sum variable
        sum += math.pow(values1[i] - values2[i], 2)
        
        #at the end, we get the sum of total and get the square root of the value
    return math.sqrt(sum)
        

def knn(train_dset, test_dset, K):
    dists, train_size = {}, len(train_dset)
    
    for i in range(train_size):
        d = euclidean_dist(train_dset[i], test_dset)
        dists[i] = d
        
        k_nearest_neighbor = sorted(dists, key=dists.get)[:K]
        
        Recommended_size, NotRecommended_size = 0, 0
        for index in k_nearest_neighbor:
            if train_dset[index][-1] == 1:
                Recommended_size += 1
            else:
                NotRecommended_size += 1
        
        if Recommended_size > NotRecommended_size:
            return 1
        else:
            return 2 
    

def info_dataset(dataset, verbose):
    if verbose:
        print('total of data: %d' % len(dataset))
        
    Recommended,  NotRecommended = 0, 0
        
    for data in dataset:
        if data[-1] == 1:
            Recommended += 1
        else:
             NotRecommended += 1
        
    if verbose:
        print('total of Recommended: %d' % Recommended)
        print('total of NotRecommended: %d' % NotRecommended)
            
    return [len(dataset), Recommended, NotRecommended]
    
#percentage of data for training
percentage_train = 0.6

_, Recommended, NotRecommended = info_dataset(dataset, verbose=False)

train_dset, test_dset = [], []
max_Recommended, max_NotRecommended = int(percentage_train * Recommended), int(percentage_train * NotRecommended)
   
total_Recommended, total_NotRecommended = 0, 0

for data in dataset:
    if (total_Recommended + total_NotRecommended) < (max_Recommended + max_NotRecommended):
        train_dset.append(data)
        
        if(data[-1] == 1 and total_Recommended < max_Recommended):
            total_Recommended += 1
        else:
            total_NotRecommended += 1
    else:
        test_dset.append(data)
        

hits, K = 0, 15

for data in test_dset:
    result = knn(train_dset, data, K)
    if data[-1] == result:
        hits += 1
        
print('total of train dataset: %d' % len(train_dset))
print('Total of test dataset: %d' % len(test_dset))
print('Total of hits: %d' % hits)
print('percentage of hits: %.2f%% ' % (100 * hits / len(test_dset))) 
                 


