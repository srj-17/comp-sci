from neuron import Neuron
from utility import getInput, getTarget

"""
Program to train the given training set
and predict class for the input (6, 82)
and (5.3, 52)

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

raw_training_data = [
    [5.9, 75, -1],
    [5.8, 86, -1],
    [5.2, 50, 1],
    [5.4, 55, 1],
    [6.1, 85, -1],
    [5.5, 62, -1],
]

maxX0 = max(x[0] for x in raw_training_data)
minX0 = min(x[0] for x in raw_training_data)
maxX1 = max(x[1] for x in raw_training_data)
minX1 = min(x[1] for x in raw_training_data)

# normalized
training_data = [
    [(x[0] - minX0) / (maxX0 - minX0), (x[1] - minX1) / (maxX1 - minX1), x[2]]
    for x in raw_training_data
]

rawTestData = [[6, 82], [5.3, 52]]

# normalized
testData = [
    [(x[0] - minX0) / (maxX0 - minX0), (x[1] - minX1) / (maxX1 - minX1)]
    for x in rawTestData
]


newWeights = [0, 0]
newBias = 0

learningRate = 1

neuron = Neuron(2)

noOfEpoch = 4


def trainNeuron():
    for sample in training_data:
        x = getInput(sample)
        t = getTarget(sample)
        y = neuron.threashold(x)

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


def testNetwork(neuron, testData):
    testOutputs = []
    for data in testData:
        output = neuron.threashold(data)
        testOutputs.append(output)

    return testOutputs


for i in range(noOfEpoch):
    trainNeuron()

print(
    "Test output :",
    ["Male" if x == -1 else "Female" for x in testNetwork(neuron, testData)],
)
