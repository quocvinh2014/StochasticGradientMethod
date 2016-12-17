import numpy as np

temporary = np.array([0.1,0.1,0.1])
theta = temporary

def gradient_decent(theta, targets, data, learning_rate):
    theta_temp = temporary
    for i in range(0, len(targets)):
        predict = theta[0] + theta[1] * data[i][0] + theta[2] * data[i][1]
        error = targets[i] - predict

        theta_temp[0] = theta[0] + learning_rate * error
        for j in range (1, len(theta)):
            theta_temp[j] = theta[j] + learning_rate * error * data[i][j-1]
        theta = theta_temp

def run():
    points_x = np.genfromtxt('ex3x.dat', delimiter='   ')
    points_y = np.genfromtxt('ex3y.dat')
    gradient_decent(theta, points_y, points_x, 0.000000001)
    print(theta)

run()