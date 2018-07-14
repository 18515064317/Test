import numpy as np
from numpy import dot
from numpy import mat
from numpy.linalg import inv
import pandas as pd
#
# A = np.mat([1, 2])
# print('A:\n', A)
# print('A.T:\n', A.T)
# print(A.reshape(2, 1))
# print('=============')
# AT = A.T
# B = np.mat([[2, 4], [3, 5]])
# print('B:\n', B)
# print('B的逆:\n', inv(B))
#
# # A 1*2 B 2*2
# print('B.A:\n', B.A)
# print('A.B:\n', AT.B)
#
# C = np.array([2, 3])
# print('C:\n',C)

# y = 2x
# X = np.mat([1, 2, 3]).reshape(3, 1)
# Y = 2*X
# print('X:\n', X)
# print('Y:\n', Y)
# print('X.T:', X.T)
# print('X[0:]-------', X[0:])
# print('dot(X.T, X):==', dot(X.T, X))
# print('inv(dot(X.T, X)):::',inv(dot(X.T, X)))
# print('dot(inv(dot(X.T, X)), X.T::::',dot(inv(dot(X.T, X)), X.T))
# #求值theta
# theta = dot(dot(inv(dot(X.T, X)), X.T), Y)
# print('dot(dot(inv(dot(X.T, X)), X.T), Y)::--', theta)

dataset = pd.read_csv('data.csv')
print(dataset)
temp = dataset.iloc[:, 2:5]
temp['x0'] = 1
X = temp.iloc[:, [3, 0, 1, 2]]
print('-------------\n', X)
Y = dataset.iloc[:, 1]
print('===========\n', Y)

# theta = dot(dot(inv(dot(X.T, X)), X.T), Y)
# print(']]]]]]]]]]]]]]]]]\n', theta.reshape(4, 1))