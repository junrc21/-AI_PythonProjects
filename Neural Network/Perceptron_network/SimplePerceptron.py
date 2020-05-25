#Perceptron implementation
import random

class Perceptron:

    def __init__(self, _inputs, _outputs, tax=0.5, age=100, limiar=-1):
        self._inputs = _inputs
        self._outputs = _outputs
        self.tax = tax
        self.age = age
        self.limiar = limiar
        self.n_inputs = len(_inputs)
        self.n_attrb = len(_inputs[0])
        self.weights = []
        
    def train(self):
        for data in self._inputs:
            data.insert(0, -1)

        #add random weights to the weights array
        for i in range(self.n_attrb + 1):
            self.weights.append(random.random())

        #insert limiar to weights array
        self.weights.insert(0, self.limiar)
        n_age = 0 #Age counnter
        
        while True: 
            error = False #At the beginning, the error don't exist
            
            for i in range(self.n_inputs):
                u = 0 #sum of inputs and weights
                for j in range(self.n_attrb + 1):
                    u += self.weights[j] * self._inputs[i][j] 
                
                #call activation function
                y = self.degrau(u)  #get network output   
                
                #Test if network output is different from the expected output
                if y != self._outputs[i]:
                    error_adj = self._outputs[i] - y #calc the error adjust for use to weight adjustment
                    
                    #adjust the weights
                    for j in range(self.n_attrb + 1):
                        self.weights[j] = self.weights[j] + self.tax * error_adj * self._inputs[i][j]                        
                    error = True #The error remains                

            #increase n_ages value
            n_age += 1              
                      
            #Stop criteria
            if not error or n_age > self.age:
                break

    #activation function
    def degrau(self, u):
        if u >= 0:
            return 1
        return 0

    #activation function
    def test(self, _input):
        _input.insert(0, -1)
        
        u = 0
        for i in range(self.n_attrb + 1):
            u += self.weights[i] * _input[i]

        #call activation function    
        y = self.degrau(u)
        
        #print result
        return print('Output: %d' % y)
             
 #create arrays with values      
_inputs = [[0.,0], [0,1], [1,0], [1,1]]
_outputs = [0, 1, 1, 1]
        
#call class functions
network = Perceptron(_inputs, _outputs)
network.train()
network.test([1, 0])