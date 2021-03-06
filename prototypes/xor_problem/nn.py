import numpy as np
import sys


# linear combination
# v0*w0 + v1*w1 + ... + vk*wk + bias
def lin(InputVector, WeightVector, bias):
    res = 0
    for i, j in zip(InputVector, WeightVector):
        res += i * j
    return res + bias


# rectified Linear Unit
def relu(x):
    return max(0, x)


# derivative of ReLU
def relu_p(x):
    return int(x > 0)


# loss function
def err(prediction, target):
    return (prediction - target) ** 2


# learning procedure
def learn(W, b, sample, target, learning_rate):
    # dot product
    z = lin(sample, W, b)
    # activation function
    u = relu(z)
    # backpropagation
    for i in range(len(sample)):
        # dL_dw === lin'(I, w, b) with respect to 'w'
        dL_dw = sample[i]
        # dR_dL === relu'(L)
        dR_dL = relu_p(z)
        # derr_dR === d(err)/d(prediction)
        derr_dR = 2 * (u - target)
        # delta error
        derr_dw = derr_dR * dR_dL * dL_dw
        # improve weights
        W[i] -= derr_dw * learning_rate
    # dL_db === lin'(I, w, b) with respect to 'b'
    dL_db = 1
    derr_db = derr_dR * dR_dL * dL_db
    # improve bias
    b -= derr_db * learning_rate

    return W, b


# predict an output
def predict(Input, ExpectedOutput, W, b, info=True):
    z = lin(Input, W, b)
    u = relu(z)
    cost = err(u, ExpectedOutput)
    actual = ExpectedOutput
    if info:
        print("Values:    \t{}\nPrediction:\t{}".format(
            Input, u))
        print("Actual value:\t{}\nLoss:      \t{}".format(
            actual, err(u, actual)))
    return {"out": u, "cost": cost}


dataset = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]


# The single-layer perceptron is unable to solve XOR Problem
# MultiLayer Perceptron is required
def main():
    W, b = [np.random.normal(), np.random.normal()], np.random.normal()
    learning_rate = 0.00001
    reps = 100000
    if len(sys.argv) > 1:
        W = eval(sys.argv[1])
        b = eval(sys.argv[2])

    for i in range(reps):
        R = dataset[np.random.randint(len(dataset))]
        Input = R[:-1]
        Output = R[2]
        W, b = learn(W, b, Input, Output, learning_rate)

    for v in dataset:
        predict(v[:-1], v[2], W, b)
        print()

    print("'{}' {}".format(W, b))


if __name__ == "__main__":
    main()
