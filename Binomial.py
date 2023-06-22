import numpy as np
import matplotlib.pyplot as plt

n = 50 # Number of trials
p = 0.5 # Probability of success
binom_rv = np.random.binomial(n, p, 10000)
plt.hist(binom_rv, bins=n+1, density=True, alpha=0.6, color='b')
x = np.arange(0, n+1)
pmf = np.zeros(n+1)
for k in x:
    pmf[k] = np.math.comb(n, k) * p**k * (1-p)**(n-k)
plt.plot(x, pmf, 'r', linewidth=2)
plt.title('Binomial Random Variable')
plt.xlabel('Number of Successes')
plt.ylabel('Probability Mass')
plt.show()
