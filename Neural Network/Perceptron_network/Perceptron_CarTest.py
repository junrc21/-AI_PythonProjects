import numpy as np 
import random

class Perceptron_CarTest: 

    def __init__(self, _inputs, _outputs, tax=0.3, age=100000, limiar=-1):
        self._inputs = _inputs
        self._outputs = _outputs
        self.tax = tax
        self.age = age
        self.limiar = limiar
        
        self.n_elements = len(_inputs)
        self.n_attrb = len(_inputs[0])
        self.weights = []
        
    def train(self):
        #insert -1 to the array
        for data in self._inputs:
            data.insert(0, -1)

        #setting weights
        for i in range(self.n_attrb + 1):
            self.weights.append(random.random())

        #insert limiar to the weights array
        self.weights.insert(0, self.limiar)        
        n_age = 0   
        
        while True:
             error = False #At the beginning, the error don't exist
             
             for i in range(self.n_elements):
                 u = 0 #sum of inputs and weights
                 
                 for j in range(self.n_attrb + 1):
                     u += self.weights[j] * self._inputs[i][j]
            
                #call activation function
                 y = self.degrau(u)  #get network output  
                
                #Test if network output is different from the expected output
                 if y != self._outputs[i]:
                    error_adj = self._outputs[i] - y
                    
                    #adjust the weights
                    for j in range(self.n_attrb + 1):
                        self.weights[j] = self.weights[j] + self.tax * error_adj * self._inputs[i][j]                        
                    error = True #The error remains  
                
             n_age += 1     
            
            #Stop criteria
             if not error:
                 print('....................  FINISHED ..............................')
                 print('Results:')
                 print('ages: %d' % n_age)
                 print('weights: %s' % self.weights)
                 break

             if n_age >= self.age:
                 print('....................  ABORTING ..............................')
                 break
        
    #activation function        
    def degrau(self, u):
        if u >= 0:
            return 1
        return 0

    #activation function
    def degrauBipilar(self, u):
        if u >= 1:
            return 1
        elif u < 0:
            return -1
        else:
            return 0     

    #test method
    def test(self, input):
         #self.weights = [-30.40000000000005, 88.81114093386655, 30.39568548100507, -26.009534144024723, -37.78980191298465, -24.5201673508826, -49.18643282910237, 0.2269911524616247]
         input.insert(0, -1)

         u = 0
         for i in range(self.n_attrb + 1):
            u += self.weights[i] * input[i]

         #call activation function
         y = self.degrau(u)

         #return the value
         return print('Output: %d' % y)

                  
             
#create arrays
input, output = [], []

#load data from file
with open('C:\AI Projects\AI_Datasets\car.data', 'r') as file:
    for line in file.readlines():
        atrb = line.replace('\n', '').split(',')
        input.append([int(atrb[0]), int(atrb[1]), int(atrb[2]), int(atrb[3]),
                    int(atrb[4]), int(atrb[5])])
        output.append(int(atrb[6]))

#call class functions
print('....................  STARTING ..............................')
network = Perceptron_CarTest(input, output)
network.train()

#test
print('\n\nRunning a test:')
network.test([3,1,3,4,2,0])