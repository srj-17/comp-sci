def getInput(sample):
    return sample[:-1]


def getTarget(sample):
    return sample[-1]


class Neuron:
    """
    A class to simulate a neuron

    constructor parameters: weights (array), bias(array)
    """

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

        for x in inputs:
            total += x * self.weights[inputs.index(x)]

        return total + self.bias

    def threashold(self, inputs):
        """
        Returns 1 if the sum of weight * input > threashold,
        0 otherwise.

        Returns:
            int: 1 or 0
        """

        output = self.calculateOutput(inputs)

        if output > 0:
            return 1

        if output == 0:
            return 0

        return -1

    def update(self, newWeights, newBias):
        self.weights = newWeights
        self.bias = newBias


if __name__ == "__main__":
    training_data = [
        [1, 1, 1],
        [1, -1, -1],
        [-1, 1, -1],
        [-1, -1, -1],
    ]

    testData = [-1, -1]  # should output -1

    NO_OF_SAMPLES = len(training_data)

    prevWeights = [0, 0]
    prevBias = 0

    newWeights = None
    newBias = None

    learningRate = 1
    # Weights and bias are initialized as 0
    neuron = Neuron(prevWeights, prevBias)

    for sample in training_data:
        x = getInput(sample)
        t = getTarget(sample)
        y = neuron.threashold(x)
        newWeights = [
            w + learningRate * (t - y) * x[neuron.weights.index(w)]
            for w in neuron.weights
        ]
        newBias = neuron.bias + learningRate * (t - y)
        neuron.update(newWeights, newBias)
        print(
            "Current bias: ",
            neuron.bias,
            "Current weights: ",
            neuron.weights,
        )

    testResult = neuron.threashold(testData)

    print("Test result :", testResult)
