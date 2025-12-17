"""
Program to train a perceptron with the given
training set and predict class for the input 
(6, 82) and (5.3, 52)

Training data provided:
    Height(x1) Weight(x2) Class(t)
        5.9     75          Male
        5.8     86          Male
        5.2     50          Female
        5.4     55          Female
        6.1     85          Male
        5.5     62          Male

Note that we've represented Male as -1
and female as 1
"""

from neuron import Neuron
from utility import train_neuron, test_network, normalize_training_data

# get inputs and test data
raw_training_data = [
    [5.9, 75, -1],
    [5.8, 86, -1],
    [5.2, 50, 1],
    [5.4, 55, 1],
    [6.1, 85, -1],
    [5.5, 62, -1],
]

raw_test_data = [[6, 82], [5.3, 52]]

# normalize data
training_data, test_data = normalize_training_data(raw_training_data, raw_test_data)

# create a perceptron
neuron = Neuron(2)

# train the perceptron
NO_OF_EPOCH = 4
for i in range(NO_OF_EPOCH):
    train_neuron(neuron, training_data)

# test the perceptron
print(
    "Test output :",
    ["Male" if x == -1 else "Female" for x in test_network(neuron, test_data)],
)
