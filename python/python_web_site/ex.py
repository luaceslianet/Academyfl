import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
 
# Generate sample data
np.random.seed(0)
lifespan = np.random.randint(1, 100, 100)  # Lifespan of machinery parts (in months)
failure_time = lifespan**2 / 100 + np.random.randint(-10, 10, 100)  # Failure time (in months)
 
# Reshape the data
lifespan = lifespan.reshape(-1, 1)
 
# Plot the data
plt.figure(figsize=(8, 6))
plt.scatter(lifespan, failure_time, color='blue', label='Original Data')
 
# Iterate over different polynomial degrees
for degree in range(1, 5):
    # Create polynomial regression model
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
 
    # Fit the model
    model.fit(lifespan, failure_time)
 
    # Predict
    x_values = np.linspace(min(lifespan), max(lifespan), 100).reshape(-1, 1)
    y_values = model.predict(x_values)
 
    # Plot the polynomial regression curve
    plt.plot(x_values, y_values, label='Degree {}'.format(degree))
 
plt.title('Machinery Failure Prediction (Polynomial Regression)')
plt.xlabel('Lifespan (months)')
plt.ylabel('Failure Time (months)')
plt.legend()
plt.grid(True)
plt.show()