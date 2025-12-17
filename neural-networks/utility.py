def getInput(sample):
    return sample[:-1]

def getTarget(sample):
    return sample[-1]

def train_neuron(neuron, training_data):
    """
    Train a neuron with learning_rate = 1
    and threashold activation function
    """

    new_weights = None
    new_bias = None
    learning_rate = 1

    for sample in training_data:
        # get input sample
        x = getInput(sample)
        t = getTarget(sample)

        # find calculate output and apply 
        # threashold activation function
        y = neuron.threashold(x, threashold=0)

        # calculate new parameters based on error
        new_weights = [
            neuron.weights[i] + learning_rate * (t - y) * x[i]
            for i in range(len(x))
        ]
        new_bias = neuron.bias + learning_rate * (t - y)

        # update the parameters
        neuron.update(new_weights, new_bias)

        # print current parameters for diagnostics
        print(
            "Current bias: ",
            neuron.bias,
            "Current weights: ",
            neuron.weights,
        )

def test_network(neuron, testData):
    testOutputs = []
    for data in testData:
        output = neuron.threashold(data)
        testOutputs.append(output)

    return testOutputs

def normalize_training_data(raw_training_data, raw_test_data):
    """
    Max normalize the given data
    the input should be of the form
    raw_training_data = [
        [int, int, int]
        [int, int, int]
    ]

    raw_test_data = [
        [int, int]
        [int, int]
    ]
    """
    maxX0 = max(x[0] for x in raw_training_data)
    minX0 = min(x[0] for x in raw_training_data)
    maxX1 = max(x[1] for x in raw_training_data)
    minX1 = min(x[1] for x in raw_training_data)

    # normalized
    normalized_training_data = [
        [(x[0] - minX0) / (maxX0 - minX0), (x[1] - minX1) / (maxX1 - minX1), x[2]]
        for x in raw_training_data
    ]

    normalized_test_data = [
        [(x[0] - minX0) / (maxX0 - minX0), (x[1] - minX1) / (maxX1 - minX1)]
        for x in raw_test_data
    ]

    return normalized_training_data, normalized_test_data
