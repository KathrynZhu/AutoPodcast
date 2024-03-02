import matplotlib.pyplot as plt
import numpy as np

# Define the input range
x = np.linspace(-5, 5, 100)

# Compute the output of the linear activation function
y = x

# Plot the linear activation function
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Linear Activation', color='b')
plt.title('Linear Activation Function')
plt.xlabel('Input')
plt.ylabel('Output')
plt.grid(True)
plt.legend()
plt.show()
