import numpy as np

np.random.seed(42)

students = np.array([1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1])
print(students.mean())
sample = np.random.choice(students, 21)
print(sample.mean())

proportions = [np.random.choice(students, 21).mean() for _ in range(10000)]

import matplotlib.pyplot as plt

plt.hist(proportions)
plt.show()
