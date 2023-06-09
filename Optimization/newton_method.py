import numpy as np
x0 = np.array([0,0,0]).T
f = lambda x: x[0]**2 + x[1]**2 + x[2]**2 - x[0]*x[1] - x[1]*x[2] + x[0] + x[2]
df = lambda x: np.array([2*x[0] - x[1] + 1, 2*x[1] - x[0] -x[2], 2*x[2] - x[1] + 1])
ddf = np.array([[2,-1,0], [-1,2,-1], [0,-1,2]]) 
k = 0
x = x0
iH = np.linalg.inv(ddf).T
print('Initial solution x0 = ',x0,'; f(x0) = ', f(x0))
while True:
    D = df(x).T
    h = iH.dot(D)
    x = x - h
    print('new solution: ',x,'; f(x) = ', f(x))
    k = k + 1
    if k > 10000 or np.linalg.norm(h) < 0.0001:
        break