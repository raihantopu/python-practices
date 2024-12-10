import matplotlib.pyplot as plt
import numpy as np
import random

xpoints = np.random.randint(10, 1000, size=20)
ypoints = np.random.randint(10, 100, size=20)

plt.plot(xpoints, ypoints)
plt.show()
