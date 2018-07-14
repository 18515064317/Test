import numpy as np

a = np.array([1, 3, 2])
a = a.reshape(3, -1)
print(a)
print(a.shape)

b = np.zeros((3, 4))
print(b)
a = np.full((3, 4), 3)
print(a)
a = np.eye(5)
print(a)
a = np.random.random((4, 5))
print(a)

c = np.array([[1, 2, 4, 5, 8],
              [15, 52, 54, 55, 548],
              [13, 24, 44, 54, 84],
              [11, 12, 14, 15, 18],
              [21, 22, 42, 27, 812]])
print(c[-2:, 1:6])
print(c[4:, -3])
print(c.shape)
print(c.dtype)

d = np.array([1, 2, 2334.21])
print(d.dtype)
d1 = np.array(d, dtype = np.int64)
print(d1)
print(d1.dtype)

a = np.array([[1, 4, 2, 3],
              [2, 5, 6, 7]])
b = np.array([[11, 14, 72, 83],
              [22, 52, 62, 72]])
# + 加法 用add函数 ## a + b 与 np.add(a, b) 是一样的
# -  加法 用subtract函数 ## a - b 与 np.subtract(a, b) 是一样的
# * 加法 用multiply函数 ## a * b 与 np.multiply(a, b) 是一样的
# / 加法 用divide函数 ## a / b 与 np.divide(a, b) 是一样的
print(a + b)
print(np.add(a, b))
print(a - b)
print(np.subtract(a, b))
print(a * b)
print(np.multiply(a, b))
print(a / b)
print(np.divide(a, b))

a = np.array([[1, 2, 3],
              [3, 4, 5]])
b = np.array([[1, 2, 3, 9],
              [3, 4, 5, 8],
              [2, 5, 6, 7]])
print(a.dot(b))
print(np.sum(a))
print(np.sum(a, axis = 0))
print(np.random.uniform(3, 5))

print(np.tile(a,(3,2)))
print(np.argsort(a))
print(a.T)

