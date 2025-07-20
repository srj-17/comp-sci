"""
Program to create a neuron and predict it's
output using threashold activation function.

The weights are randomly initiated. We expect
the input initializations to be passed in as
arguments to the constructor.
"""

import random


class Neuron:
    def __init__(self, weights, bias):
        """
        Accepts an input array where the first n - 1
        elements are the inputs (x(i) values) and the last 1
        element is the output element

                Prameters:
                    inputs: array[int]
        """
        self.weights = weights
        self.bias = bias

    def calculateOutput(self, inputs):
        total = 0

        for i in inputs:
            total += i * self.weights[inputs.index(i)]

        return total + self.bias

    def threashold(self, inputs):
        """
        Returns 1 if the sum of weight * input > threashold,
        0 otherwise.

        Returns:
            int: 1 or 0
        """

        output = self.calculateOutput(inputs)

        if output > 30:
            return 1

        return -1

    def update(self, newWeights, newBias):
        self.weights = newWeights
        self.bias = newBias


if __name__ == "__main__":
    inputs = [1, 2, 3, 4, 5]
    neuron = Neuron([random.random() * 4 for _ in inputs], random.random())
    print(neuron.threashold(inputs))
