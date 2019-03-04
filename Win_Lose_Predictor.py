#predictor for gamse like COD: team deathmatch 
#Input kills and deaths into array to make your own data
from matplotlib import pyplot as plt
import numpy as np
import os
import win32com.client as winvoice

voice = winvoice.Dispatch("SAPI.SpVoice")

# each point (0 or 1)
data = [[25, 9, 1],
        [13, 9, 0],
        [17, 5, 1],
        [12, 10, 0],
        [17, 8, 1],
        [12, 9, 0],
        [23, 1, 1],
        [15, 12, 0]]

mystery_game = [19, 12]

# network
#
#     o   win or lose
#    / \   w1 , w2, b
#   o   o  kills, deaths




def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_p(x):
    return sigmoid(x) * (1 - sigmoid(x))


X = np.linspace(-6, 6, 100)
plt.plot(X, sigmoid(X), c='r')
plt.plot(X, sigmoid_p(X), c='b')
plt.show()

#scatter data
plt.axis([0, 30, 0, 30])
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
    z = point[0] * w1 + point[1] * w2 + b
    pred = sigmoid(z)
    print("prediction: {}".format(pred))

#mystery point prediction
os.system("say hi")
def which_game(lenght, width):
    z = lenght * w1 + width * w2 + b
    pred = sigmoid(z)
    if pred < .5:
        voice.speak('lose')
    else:
        voice.speak('win')

which_game(18, 4)
