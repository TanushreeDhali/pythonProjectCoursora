def boundary_value(value):

    if value<10 or value>15:
        print("false")
    else:
        print("true")

boundary_value(10)
boundary_value(15)
boundary_value(9)
boundary_value(16)

def double_word(word):
    result=word*2
    return result + str(len(result))


print(double_word("hello"))  # Should return hellohello10
print(double_word("abc"))  # Should return abcabc6
print(double_word(""))  # Should return 0


def first_and_last(message):
    if len(message)==0:
        return True
    else:
        return message[-1]==0




print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


fruite = "Mange"
print(fruite[1:-1])
print(fruite[1:-2])
print(fruite[:-2])
print(fruite[1:])

message="i hafe a car"
message.index("h")
new_message=message[0:4]+"v"+message[5:]

pets="cat & dogs"
pets.index("&")

import numpy as np


class NeuralNetwork():

    def __init__(self):
        # seeding for random number generation
        np.random.seed(1)

        # converting weights to a 3 by 1 matrix with values from -1 to 1 and mean of 0
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        # applying the sigmoid function
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        # computing derivative to the Sigmoid function
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        # training the model to make accurate predictions while adjusting weights continually
        for iteration in range(training_iterations):
            # siphon the training data via  the neuron
            output = self.think(training_inputs)

            # computing error rate for back-propagation
            error = training_outputs - output

            # performing weight adjustments
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            self.synaptic_weights += adjustments

    def think(self, inputs):
        # passing the inputs via the neuron to get output
        # converting values to floats

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


if __name__ == "__main__":
    # initializing the neuron class
    neural_network = NeuralNetwork()

    print("Beginning Randomly Generated Weights: ")
    print(neural_network.synaptic_weights)

    # training data consisting of 4 examples--3 input values and 1 output
    training_inputs = np.array([[0, 0, 1],
                                [1, 1, 1],
                                [1, 0, 1],
                                [0, 1, 1]])

    training_outputs = np.array([[0, 1, 1, 0]]).T

    # training taking place
    neural_network.train(training_inputs, training_outputs, 15000)

    print("Ending Weights After Training: ")
    print(neural_network.synaptic_weights)

    user_input_one = str(input("User Input One: "))
    user_input_two = str(input("User Input Two: "))
    user_input_three = str(input("User Input Three: "))

    print("Considering New Situation: ", user_input_one, user_input_two, user_input_three)
    print("New Output data: ")
    print(neural_network.think(np.array([user_input_one, user_input_two, user_input_three])))
    print("Wow, we did it!")
