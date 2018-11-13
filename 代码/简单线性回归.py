import numpy as np

def fitSLR(x, y):
    n = len(x)
    dinominator = 0
    numerator = 0
    for i in range(0, n):
        numerator += (x[i] - np.mean(x))*(y[i] - np.mean(y))
        dinominator += (x[i] - np.mean(x))**2
    b1 = numerator/float(dinominator)
    b0 = np.mean(y)-b1*np.mean(x)
    return b0, b1

def predict(x, b0, b1):
    return b0 + x*b1

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y = [425, 358, 434, 445, 527, 429, 426, 502, 480, 385, 427, 446, 478]    

b0, b1 = fitSLR(x, y)
print("intercept:", b0, " slope:", b1)
x_test = 14
y_test = predict(14, b0, b1)
print("y_test:", y_test)
