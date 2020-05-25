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
        #get euclidean distance value
        d = euclidean_dist(train_dset[i], test_dset)

        #add distance to array
        dists[i] = d

        #get the keys of the K-nearest neighbors, the less distance (less value)
        k_nearest_neighbor = sorted(dists, key=dists.get)[:K]

        #inicialize lablels values
        Recommended_size, NotRecommended_size = 0, 0

        #for each K-nearest neighbors found do:        
        for index in k_nearest_neighbor:
            
            #if the label (last element from array) is == 1 then icrease the label1, else increase label2 
            if train_dset[index][-1] == 1:
                Recommended_size += 1
            else:
                NotRecommended_size += 1

        #at the end, return wich label has more 
        if Recommended_size > NotRecommended_size:
            return 1
        else:
            return 2 
    

def info_dataset(dataset, verbose):
    if verbose:
        print('total of data: %d' % len(dataset))

    #create labels    
    Recommended,  NotRecommended = 0, 0

    #increase labels values according file label
    for data in dataset:
        #get the lable (-1 means the last element)
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

#get label lenght for label1 and lablel2
_, Recommended, NotRecommended = info_dataset(dataset, verbose=False)

#create dataset arrays
train_dset, test_dset = [], []

#get the max values to get from file to use for training
max_Recommended, max_NotRecommended = int(percentage_train * Recommended), int(percentage_train * NotRecommended)
   
total_Recommended, total_NotRecommended = 0, 0

#add values to the training and testing datasets
for data in dataset:

    #if total is not reached, can add more elements to traing dataset
    #else, will add the rest to training dataset
    if (total_Recommended + total_NotRecommended) < (max_Recommended + max_NotRecommended):
        train_dset.append(data)
        
        if(data[-1] == 1 and total_Recommended < max_Recommended):
            total_Recommended += 1
        else:
            total_NotRecommended += 1
    else:
        test_dset.append(data)

#set K value       
hits, K = 0, 15

#execute predict for each testing dataset element 
for data in test_dset:
    result = knn(train_dset, data, K)
    if data[-1] == result:
        hits += 1

#print info
print('total of train dataset: %d' % len(train_dset))
print('Total of test dataset: %d' % len(test_dset))
print('Total of hits: %d' % hits)
print('percentage of hits: %.2f%% ' % (100 * hits / len(test_dset))) 
                 


