import numpy as np
import matplotlib.pyplot as plt

mu, b = 0, 1 
laplacian_rv = np.random.laplace(mu, b, 1000)


plt.hist(laplacian_rv, bins=50, density=True, alpha=0.6, color='g')
x = np.linspace(-10, 10, 1000)
pdf = 1/(2*b) * np.exp(-abs(x-mu)/b)
plt.plot(x, pdf, 'r', linewidth=2)
plt.title('Laplacian Random Variable with c=1')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.show()
