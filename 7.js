import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg') # Use TkAgg backend
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
# Load California Housing dataset for Linear Regression
data = fetch_california_housing(as_frame=True)
X = data.data[['AveRooms']]
y = data.target
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)
# Linear Regression
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)
y_pred = linear_reg.predict(X_test)
# Polynomial Regression
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X_train)
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y_train)
y_pred_poly = poly_reg.predict(poly.fit_transform(X_test))
# Plotting results
plt.subplot(1, 2, 1)
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.title('Linear Regression')
plt.subplot(1, 2, 2)
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred_poly, color='green')
plt.title('Polynomial Regression')
plt.tight_layout()
plt.show()
# Output MSE
print(f"Linear Regression - MSE: {mean_squared_error(y_test, y_pred):.4f}")
print(f"Polynomial Regression - MSE: {mean_squared_error(y_test,
y_pred_poly):.4f}")
