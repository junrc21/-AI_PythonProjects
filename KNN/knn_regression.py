import math
import matplotlib.pyplot as plt 
import numpy as np 

class KNN_Regression:
    
    def __init__(self, x, y, k=3):
        self.n_samples = len(x)
        self.n_atrb = len(x[0])
        self.x, self.y, self.k = x, y, k
        
    def predict(self, data):
        d = {}
        for i in range(self.n_samples):
            sum_ = 0
            for j in range(self.n_atrb):
                sum_ += math.pow(data[j] - self.x[i][j], 2)
            d[i] = math.sqrt(sum_)
        
        knn = sorted(d, key=d.get)[:self.k]
        _sum = sum([self.y[index] for index in knn])
        
        return _sum / self.k
    
if __name__ == "__main__":
    inputs = [[2.50], [4.90], [1.38], [5.105], [2.48], [6.120], [3.65], [4.80], [5.100], [3.60]]
    outputs = [250, 490, 138, 505, 248, 612, 365, 480, 500, 360]

    knn = KNN_Regression(inputs, outputs, 3)
    result = []
    for input in inputs:
        result.append(knn.predict(input))
        
    plt.plot(np.linspace(-1, 1, 10), outputs, label='expected', color='blue')
    plt.plot(np.linspace(-1, 1, 10), result, label='result', color='black')
    plt.show()
            
        
            
