"""
Program to create a neuron and predict it's
output using threashold activation function.

The weights are randomly initiated. We expect
the input initializations to be passed in as
arguments to the constructor.
"""


class Neuron:
    def __init__(self, noOfInputs):
        """
        Accepts an input array where the first n - 1
        elements are the inputs (x(i) values) and the last 1
        element is the output element

        Bias and weights are initialized to 0 by default.

                Prameters:
                    inputs: array[int]
        """
        self.weights = [0] * noOfInputs
        self.bias = 0

    def calculateOutput(self, inputs):
        total = 0

        for i in inputs:
            total += i * self.weights[inputs.index(i)]

        return total + self.bias

    def threashold(self, inputs, threashold=0.5):
        """
        Returns 1 if the sum of weight * input > threashold,
        0  if < threashold and 0.5 otherwise

        Returns:
            int: 1 or -1 or 0
        """

        output = self.calculateOutput(inputs)

        if output > threashold:
            return 1

        if output < threashold:
            return -1

        return 0

    def update(self, newWeights, newBias):
        self.weights = newWeights
        self.bias = newBias


if __name__ == "__main__":
    inputs = [1, 2, 3, 4, 5]
    neuron = Neuron([random.random() * 4 for _ in inputs], random.random())
    print(neuron.threashold(inputs))
