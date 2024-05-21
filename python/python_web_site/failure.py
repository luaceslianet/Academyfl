import numpy as np

import matplotlib.pyplot as plt
 
# Generate sample data

np.random.seed(0)

lifespan = np.random.randint(1, 100, 100)  # Lifespan of machinery parts (in months)

failure_time = lifespan + np.random.randint(-10, 10, 100)  # Failure time (in months)
 
# Perform linear regression

slope, intercept = np.polyfit(lifespan, failure_time, 1)
 
print("Slope:", slope)

print("Intercept:", intercept)
 
# Plot the data and regression line

plt.figure(figsize=(8, 6))

plt.scatter(lifespan, failure_time, color='blue', label='Original Data')

plt.plot(lifespan, slope * lifespan + intercept, color='red', label='Linear Regression Line')

plt.title('Machinery Failure Prediction')

plt.xlabel('Lifespan (months)')

plt.ylabel('Failure Time (months)')

plt.legend()

plt.grid(True)

plt.show()
