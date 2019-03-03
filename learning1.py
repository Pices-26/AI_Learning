from matplotlib import pyplot as plt
import numpy as np
import os

import win32com.client as wincl
voice = wincl.Dispatch("SAPI.SpVoice")

# each point (0 or 1)
data = [[3, 1.5, 1],
        [2, 1, 0],
        [4, 1.5, 1],
        [3, 1, 0],
        [3.5, 0.5, 1],
        [2, 0.5, 0],
        [5.5, 1, 1],
        [1, 1, 0]]

mystery_flower = [4.5, 1]

# network
#
#     o   flower type
#    / \   w1 , w2, b
#   o   o  lenght width




def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_p(x):
    return sigmoid(x) * (1 - sigmoid(x))


X = np.linspace(-6, 6, 100)
plt.plot(X, sigmoid(X), c='r')
plt.plot(X, sigmoid_p(X), c='b')
plt.show()

#scatter data
plt.axis([0, 8, 0, 8])
plt.grid
for i in range(len(data)):
    point = data[i]
    color = "r"
    if point[2] == 0:
        color = "b"
    plt.scatter(point[0], point[1], c=color)
plt.show()

#training loop

learning_rate = 0.2
costs = []

w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

for i in range(100000):
    ri = np.random.randint(len(data))
    point = data[ri]


    z = point[0] * w1 + point[1] * w2 + b

    pred = sigmoid(z)

    target = point[2]
    cost = np.square(pred - target)

    costs.append(cost)

    dcost_pred = 2 * (pred - target)
    dpred_dz = sigmoid_p(z)

    dz_dw1 = point[0]
    dz_dw2 = point[1]
    dz_db = 1

    dcost_dz = dcost_pred * dpred_dz

    dcost_dw1 = dcost_pred * dz_dw1
    dcost_dw2 = dcost_pred * dz_dw2
    dcost_db = dcost_pred * dz_db

    w1 = w1 - learning_rate * dcost_dw1
    w2 = w2 - learning_rate * dcost_dw2
    b = b - learning_rate * dcost_db

plt.plot(costs)
plt.show()

#priting predictions
for i in range(len(data)):
    point = data[i]
    print(point)
    z = point[0] * w1 + point[1] *w2 +b
    pred = sigmoid(z)
    print("prediction: {}".format(pred))

#mystery point prediction
os.system("say hi")
def which_flower(lenght, width):
    z = lenght * w1 + width * w2 + b
    pred = sigmoid(z)
    if pred < .5:
        voice.speak('blue')
    else:
        voice.speak('red')

which_flower(3, 4)
