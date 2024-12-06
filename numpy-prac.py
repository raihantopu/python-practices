import numpy as np

a = np.arange(0, 100, 5)
print(a)

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

n1 = np.array(l1)
n2 = np.array(l2)
print(l1 * 5)
print(n1 * 5)

a1 = np.array([1,2,3])
a2 = np.array([[1],
              [2]])
print(a1 + a2)

a = np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20]])
print(a.shape)
print(a.reshape(5,4))
print(a.reshape(2,10))
print(a.reshape(10,2))
print(a.reshape(20,1))

print(a.flatten())
print(a.ravel())

var = [v for v in a.flat]
print(var)

print(a.transpose())
print(a.T)
print(a.swapaxes(0, 1))

print(a.min())
print(a.max())
print(a.mean())
print(a.std())
print(a.sum())
print(np.median(a))
np.savetxt("array.csv", a, delimiter=",")
print(np.loadtxt("array.csv", delimiter=","))