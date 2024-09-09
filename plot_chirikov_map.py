import matplotlib.pyplot as plt
import numpy as np

# Load data from the Fortran output file
data = np.loadtxt('chirikov_map_data.txt')
p = data[:, 0]
x = data[:, 1]

# Create the plot
plt.figure(figsize=(8, 6))
plt.scatter(x, p, s=1, color='blue')
plt.title('Chirikov Standard Map')
plt.xlabel('Position (x)')
plt.ylabel('Momentum (p)')
plt.grid(True)
plt.show()
