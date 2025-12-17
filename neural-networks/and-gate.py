"""
Program to train the given percepron
for simulating AND gate.
"""

from utility import train_neuron, test_network
from neuron import Neuron

if __name__ == "__main__":

    # Weights and bias are initialized as 0
    neuron = Neuron(2)

    training_data = [
        [1, 1, 1],
        [1, -1, -1],
        [-1, 1, -1],
        [-1, -1, -1],
    ]

    test_data = [[-1, -1]]  # should output -1

    # train perceptron twice for all cases to work
    no_of_epoch = 2

    for i in range(no_of_epoch):
        train_neuron(neuron, training_data)

    print(
        "Test output :",
        test_network(neuron, test_data),
    )
