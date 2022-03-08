import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)
N = 100
x = np.random.normal(170, 20, N)
y = x + np.random.normal(5, 25, N)
colors = np.random.rand(N)
area = (25 * np.random.rand(N))**2

df = pd.DataFrame({
    'X': x,
    'Y': y,
    'Colors': colors,
    "bubble_size":area})

plt.scatter('X', 'Y',s='bubble_size',c='Colors',alpha=0.5, data=df)
plt.xlabel("X", size=16)
plt.ylabel("y", size=16)
plt.show()