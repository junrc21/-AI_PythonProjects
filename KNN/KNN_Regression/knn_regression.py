import math
import matplotlib.pyplot as plt 
import numpy as np 

class KNN_Regression:
    
    def __init__(self, x, y, k=3):
        self.n_samples = len(x)
        self.n_atrb = len(x[0])
        self.x, self.y, self.k = x, y, k

    #predict method
    def predict(self, data):
        d = {}

        #for each value of datasets (train and test) we need to calculate the euclidean_distance  
        for i in range(self.n_samples):
            sum_ = 0
            for j in range(self.n_atrb):
                 #Sub the 2 values and raise to 2
                 #then, add it to Sum variable
                sum_ += math.pow(data[j] - self.x[i][j], 2)

            #at the end, we get the sum of total and get the square root of the value
            d[i] = math.sqrt(sum_)

        #get the keys of the K-nearest neighbors, the less distance (less value)
        knn = sorted(d, key=d.get)[:self.k]

        #sum and get the arithmetic average
        _sum = sum([self.y[index] for index in knn])        
        return _sum / self.k

#to execute on first call
if __name__ == "__main__":

    #set values to the arrays
    inputs = [[2.50], [4.90], [1.38], [5.105], [2.48], [6.120], [3.65], [4.80], [5.100], [3.60]]
    outputs = [250, 490, 138, 505, 248, 612, 365, 480, 500, 360]

    #create a KNN_Regression class instace 
    knn = KNN_Regression(inputs, outputs, 3)
    result = []

    #start prediction for each element
    for input in inputs:
        result.append(knn.predict(input))

    #plot data to compare tne predicted value with the expected
    plt.plot(np.linspace(-1, 1, 10), outputs, label='expected', color='blue')
    plt.plot(np.linspace(-1, 1, 10), result, label='result', color='black')
    plt.show()
            
        
            
