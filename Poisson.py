import numpy as np
import matplotlib.pyplot as plt

np.random.seed(12)

# Set the Poisson parameter (lambda)
lam = 6
poisson_values = np.random.poisson(lam, 10000)
plt.hist(poisson_values, bins=100, density=True, alpha=0.6, color='b')
plt.title('Poisson Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Mass')
plt.show()
