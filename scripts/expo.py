import numpy as np
from envtest import fun_expo

x = np.linspace(0,10,101)
y = np.zeros(101)

for i in range(len(x)):
    y[i] = fun_expo(x[i])

print(y)