import matplotlib
matplotlib.use('TkAgg') # Use TkAgg backend for interactive plotting
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
# Load the dataset and select a feature
data = fetch_california_housing(as_frame=True)
df = data.frame
X = df['MedInc'].values.reshape(-1, 1)
y = df['MedHouseVal'].values
# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)
# Locally Weighted Regression (LWR)
def locally_weighted_regression(X_train, y_train, X_test, tau=0.1):
predictions = []
for x in X_test:
weights = np.exp(-np.sum((X_train - x) ** 2, axis=1) / (2 * tau ** 2))
X_train_b = np.c_[np.ones((X_train.shape[0], 1)), X_train]
# Solve the weighted least squares problem using np.linalg.lstsq for
efficiency
theta, _, _, _ = np.linalg.lstsq(X_train_b * weights[:, np.newaxis],
y_train * weights, rcond=None)
# Make prediction for the current test point
X_test_b = np.c_[1, x] # Add bias term
predictions.append(X_test_b @ theta)
return np.array(predictions)
# Predict values for the test set
y_pred = locally_weighted_regression(X_train, y_train, X_test, tau=0.1)
# Plot results
plt.scatter(X_test, y_test, color='blue', label='True values')
plt.scatter(X_test, y_pred, color='red', label='Predicted values')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.title('Locally Weighted Regression (LWR)')
plt.legend()
plt.grid(True)
# Show plot (interactive window)
plt.show()
# Evaluate performance
mse = np.mean((y_pred - y_test) ** 2)
print(f"Mean Squared Error: {mse:.4f}")
