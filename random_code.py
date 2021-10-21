import matplotlib.pyplot as plt
import random

n=20
x = [random.gauss(1., 1.0) for i in range(n)]
y = [random.gauss(1., 0.5) for i in range(n)]
z = [random.gauss(20., 10.) for i in range(n)]

plt.scatter(x,y,c=z,s=z)
plt.show()




