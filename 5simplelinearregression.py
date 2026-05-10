# Python Program for Simple Linear Regression
# with Performance Metrics and Graph Plot

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

# Input data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1,2,3,4,5])

# Create model
model = LinearRegression()

# Train model
model.fit(x, y)

# Prediction
y_pred = model.predict(x)


# Plot Graph
plt.scatter(x, y, label="Actual Data")
plt.plot(x, y_pred, label="Regression Line")

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Simple Linear Regression")

plt.legend()
plt.show()



print("\nPredicted Values:")
print(y_pred)

# Performance Metrics
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("\nPerformance Metrics")
print("Mean Squared Error (MSE) =", mse)
print("R2 Score =", r2)

