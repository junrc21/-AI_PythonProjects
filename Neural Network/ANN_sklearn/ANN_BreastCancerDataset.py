from sklearn.datasets import load_breast_cancer
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Load dataset from sklearn datasets
iris = load_breast_cancer()

#put inputs and outputs value into the variables
_inputs, _outputs = iris.data, iris.target

#Split the dataset:  test_size = 0.3 means 30% from data will be used to test
#the parametrs below need to be like this: x_train, x_test, y_train and y_test to get the data correctly
train_input, test_input, train_output, test_output = train_test_split(_inputs, _outputs)

#normalize all data from training dataset
scaler = StandardScaler()
scaler.fit(train_input)
train_input = scaler.transform(train_input)
test_input = scaler.transform(test_input)

#create a MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(30, 30, 30), verbose=True)

#fit all data and start prediction
mlp.fit(train_input, train_output)
results = mlp.predict(test_input)

#print info
print('predicted: ', results)
print('expected: ',  test_output)
print('Score: ', mlp.score(test_input, test_output))

#print Weights and Bias values to use later, so you don't need to train your network again
print('\nWeights: ', mlp.coefs_)
print('\nBias values: ', mlp.intercepts_)