import numpy as np
import matplotlib.pyplot as plt

lam = 1 # Rate parameter
exp_rv = np.random.exponential(1/lam, 1000)
plt.hist(exp_rv, bins=50, density=True, alpha=0.6, color='g')

x = np.linspace(0, 10, 10000)
pdf = lam * np.exp(-lam * x)
plt.plot(x, pdf, 'r', linewidth=2)
plt.title('Exponential Random Variable')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
