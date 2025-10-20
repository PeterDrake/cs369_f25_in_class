import random

import matplotlib.pyplot as plt

# xs = range(1, 21)
# ys = [1 - 0.8**x for x in xs]

def average_distance(d):
    total = 0
    for i in range(1000):
        # Generate two points within d-dimensional hypercube
        a = [random.random() for _ in range(d)]
        b = [random.random() for _ in range(d)]
        # Compute their distance
        distance = sum([(ai - bi)**2  for ai, bi in zip(a, b)]) ** 0.5
        total += distance
    return total / 1000

xs = range(1, 51)
ys = [average_distance(d) for d in xs]

plt.plot(xs, ys)
plt.show()
