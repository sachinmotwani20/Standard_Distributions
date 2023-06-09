import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
scale = 1.0
size = 1000000
rv = np.random.rayleigh(scale, size)
rv = rv[rv > 0]

plt.hist(rv, bins=50, density=True, alpha=0.6, color='b')

x = np.linspace(0, np.max(rv), 1000)
pdf = x / scale**2 * np.exp(-x**2 / (2 * scale**2))
plt.plot(x, pdf, 'r', linewidth=2)
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Rayleigh distribution with zero standard deviation')
plt.show()
