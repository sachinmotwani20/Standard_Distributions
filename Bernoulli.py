import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

p = 0.3 #Success probability

sample = np.random.binomial(1, p, 10000)
counts = np.bincount(sample) # Count the frequency of each outcome
probs = counts / len(sample) #probabilities of each outcome

plt.vlines([0, 1], 0, [1-p, p], colors='r', linestyles='dashed')
plt.plot([0, 1], probs, 'ro')
plt.xlabel('Outcome')
plt.ylabel('Probability Density')
plt.title('Bernoulli Distribution with p = 0.3 (n=10000)')
plt.xticks([0, 1], ['Failure', 'Success'])
plt.xlim(-0.5, 1.5)
plt.show()
