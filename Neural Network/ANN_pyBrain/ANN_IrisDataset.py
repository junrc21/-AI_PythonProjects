import numpy as np 
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer
import matplotlib.pyplot as plt

class ANN:

    def __init__(self):
        self.train_input_data = []
        self.train_output_data = []

        self.test_input_data = []
        self.test_output_data = []

        self.network = []
        self.trainer = []
        
    #load and prepare data to use
    def prepareData(self):
        print('loading data...')
        _inputs = np.genfromtxt('C:\AI Projects\AI_Datasets\iris.data', delimiter=',', usecols=(0, 1, 2, 3))
        _outputs = np.genfromtxt('C:\AI Projects\AI_Datasets\iris.data', delimiter=',', usecols=(4))

        #divide the data, getting from x index to y index
        #First, split and load data for training 
        self.train_input_data = np.concatenate((_inputs[:35], _inputs[50:84], _inputs[100:135]))
        self.train_output_data = np.concatenate((_outputs[:35], _outputs[50:84], _outputs[100:135]))

        #then, get the rest of data for testing
        self.test_input_data = np.concatenate((_inputs[35:50], _inputs[85:100], _inputs[135:]))
        self.test_output_data = np.concatenate((_outputs[35:50], _outputs[85:100], _outputs[135:]))
        print('data loaded!')

    #training method
    def train(self):
        #define sample dataset layout 
        dataSet = SupervisedDataSet(4, 1)

        #add values to sample dataset 
        for i in range(len(self.train_input_data)):
            dataSet.addSample(self.train_input_data[i], self.train_output_data[i])

        #create a network instace with 6 hidden layers
        self.network = buildNetwork(dataSet.indim, 6, dataSet.outdim, bias=True)

        #prepare to training passing learningrate and momentum parameters
        self.trainer = BackpropTrainer(self.network, dataSet, learningrate=0.01, momentum=0.9)

        #start training getting info about errors
        print('Starting network training....')        
        train_errors, train_errors_values = self.trainer.trainUntilConvergence(maxEpochs=100)
        print('train finished!')

        #plot the errors and validation
        plt.plot(train_errors, 'b', train_errors_values, 'r')
        plt.show()

    #training method
    def test(self):
         #define sample dataset layout
        dataSet = SupervisedDataSet(4, 1)

        #add values to test dataset 
        for i in range(len(self.test_input_data)):
            dataSet.addSample(self.test_input_data[i], self.test_output_data[i])

        #test the dataset with verbose = True to print logs
        print('Starting test....')
        self.trainer.testOnData(dataSet, verbose=True)
        print('test finished!')

net = ANN()
net.prepareData()
net.train()
net.test()

        