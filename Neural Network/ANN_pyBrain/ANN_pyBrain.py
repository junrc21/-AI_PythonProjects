from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

#define sample dataset layout 
dataSet = SupervisedDataSet(2, 1)

#add values to sample dataset
dataSet.addSample([1,1], [0])
dataSet.addSample([1,0], [1])
dataSet.addSample([0,1], [1])
dataSet.addSample([0,0], [0])

#create a network instace with 4 hidden layers
network = buildNetwork(dataSet.indim, 4, dataSet.outdim, bias=True)

#prepare to training passing learningrate and momentum parameters
trainer = BackpropTrainer(network, dataSet, learningrate=0.01, momentum=0.99)

#start training
for epoch in range(1000):
    trainer.train()

'''
trainer.trainEpochs(1000) #simplified call
trainer.trainUntilConvergence() #train until find the convergence
'''
#define test dataset layout 
test_data = SupervisedDataSet(2, 1)

#add values to sample dataset 
test_data.addSample([1,1], [0])
test_data.addSample([1,0], [1])
test_data.addSample([0,1], [1])
test_data.addSample([0,0], [0])

#test the dataset with verbose = True to print logs
trainer.testOnData(test_data, verbose=True)
