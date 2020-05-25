from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

#Load dataset from sklearn datasets
iris = datasets.load_iris()

#put inputs and outputs value into the variables
_inputs, _outputs = iris.data, iris.target

#create a MLPClassifier
mlp = MLPClassifier(solver='adam', alpha=0.0001, hidden_layer_sizes=(5,), random_state=1, 
                    learning_rate='constant', learning_rate_init=0.01, max_iter=500,
                    activation='logistic', momentum=0.9, verbose=True, tol=0.0001)

#Split the dataset:  test_size = 0.3 means 30% from data will be used to test
#the parametrs below need to be like this: x_train, x_test, y_train and y_test to get the data correctly
train_input, test_input, train_output, test_output = train_test_split(_inputs, _outputs, test_size=0.3,
                                                                      random_state=1)
#fit all data and start prediction
mlp.fit(train_input, train_output)
results = mlp.predict(test_input)

#print info
print('predicted: ', results)
print('expected: ',  test_output)
print('Score: ', mlp.score(test_input, test_output))