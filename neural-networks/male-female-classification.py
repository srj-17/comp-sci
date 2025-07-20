from neuron import Neuron

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

Note that we've represented Male as 0
and female as 1
"""


def getInputs(training_data):
    inputs = []

    for sample in training_data:
        minSampleData = min(sample)
        maxSampleData = max(sample)

        # normalize and append
        inputs.append(
            [(x - minSampleData) / (maxSampleData - minSampleData) for x in sample[:-1]]
        )

    return inputs


def getTargets(training_data):
    outputs = []
    for sample in training_data:
        minSampleData = min(sample)
        maxSampleData = max(sample)

        # normalize and append
        outputs.append((sample[-1] - minSampleData) / (maxSampleData - minSampleData))

    return outputs


training_data = [
    [5.9, 75, 0],
    [5.8, 86, 0],
    [5.2, 50, 1],
    [5.4, 55, 1],
    [6.1, 85, 0],
    [5.5, 62, 0],
]

testData = [[6, 82], [5.3, 52]]


NO_OF_SAMPLES = len(training_data)
inputs = getInputs(training_data)
targets = getTargets(training_data)

# 2 weights for 2 inputs
prevWeights = [0, 0]
prevBias = 0

newWeights = [0, 0]
newBias = 0

learningRate = 1

neuron = Neuron(prevWeights, prevBias)

for i in range(NO_OF_SAMPLES):
    sampleInput = inputs[i]
    t = targets[i]
    y = neuron.threashold(sampleInput)

    for j in range(len(sampleInput)):
        newWeights[j] = prevWeights[j] + learningRate * (t - y) * sampleInput[j]

    newBias = prevBias + learningRate * (t - y)
    neuron.update(newWeights, newBias)

    prevBias = newBias
    prevWeights = newWeights


def testNetwork(neuron, testData):
    testOutputs = []
    for data in testData:
        output = neuron.threashold(data)
        testOutputs.append(output)

    return testOutputs


print(testNetwork(neuron, testData))
