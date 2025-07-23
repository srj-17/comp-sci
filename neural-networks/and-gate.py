from utility import getInput, getTarget
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

    testData = [-1, -1]  # should output -1

    # train perceptron twice for all cases to work
    noOfEpoch = 2

    def trainNeuron(neuron):

        newWeights = None
        newBias = None

        learningRate = 1
        for sample in training_data:
            x = getInput(sample)
            t = getTarget(sample)
            y = neuron.threashold(x, threashold=0)

            newWeights = [
                neuron.weights[i] + learningRate * (t - y) * x[i] for i in range(len(x))
            ]

            newBias = neuron.bias + learningRate * (t - y)
            neuron.update(newWeights, newBias)
            print(
                "Current bias: ",
                neuron.bias,
                "Current weights: ",
                neuron.weights,
            )

    for i in range(noOfEpoch):
        trainNeuron(neuron)

    testResult = neuron.threashold(testData, threashold=0)

    print("Test result :", testResult)
