import numpy as np
import matplotlib.pyplot as plt

std_dev = 1
samples = np.random.normal(loc=0, scale=std_dev, size=10000)
plt.hist(samples, bins=50, density=True)

x = np.linspace(-10, 10, 1000)
y = np.exp(-x**2/(2*std_dev**2))/(np.sqrt(2*np.pi)*std_dev)
plt.plot(x, y, 'r-', linewidth=2)

plt.title('Gaussian Random Variable with Mean 0 and Standard Deviation {}'.format(std_dev))
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.show()
