import numpy as np
import matplotlib.pyplot as plt


mu = 0
sigma = 1
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = (1/(np.sqrt(2*np.pi)*sigma))*np.exp(-(x-mu)**2/(2*sigma**2))
plt.plot(x, y, color='blue')

# Shade the areas corresponding to the 68-95-99 rule
plt.fill_between(x, y, where=np.logical_and(x >= mu - 3*sigma, x <= mu + 3*sigma), color='red', alpha=0.3)
plt.fill_between(x, y, where=np.logical_and(x >= mu - 2*sigma, x <= mu + 2*sigma), color='yellow', alpha=0.3)
plt.fill_between(x, y, where=np.logical_and(x >= mu - sigma, x <= mu + sigma), color='green', alpha=0.3)

plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.title('The 68-95-99 rule for normal distribution')
plt.show()
