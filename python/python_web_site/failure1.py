import numpy as np
import matplotlib.pyplot as plt
 
# Generate sample data
np.random.seed(0)
lifespan = np.random.randint(1, 100, 100)  # Lifespan of machinery parts (in months)
failure_time = (lifespan**3) / 1000 + np.random.randint(-20, 20, 100)  # Failure time (in months)
 
# Perform polynomial regression
degree = 3  # Degree of the polynomial
coefficients = np.polyfit(lifespan, failure_time, degree)
poly_function = np.poly1d(coefficients)
 
print("Polynomial Coefficients:", coefficients)
 
# Generate points for the polynomial curve
x_values = np.linspace(min(lifespan), max(lifespan), 100)
y_values = poly_function(x_values)
 
# Plot the data and polynomial curve
plt.figure(figsize=(8, 6))
plt.scatter(lifespan, failure_time, color='blue', label='Original Data')
plt.plot(x_values, y_values, color='red', label='Polynomial Regression Curve (Degree {})'.format(degree))
plt.title('Machinery Failure Prediction (Polynomial Regression)')
plt.xlabel('Lifespan (months)')
plt.ylabel('Failure Time (months)')
plt.legend()
plt.grid(True)
plt.show()
 