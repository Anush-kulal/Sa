# Program 12: Multiple Linear Regression using Iris dataset
# Source: Statistics Lab Program PDF
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

def run():
    iris = load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data['target'] = iris.target

    X = data.drop('target', axis=1)
    y = data['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("Mean Squared Error:", mse)
    print("R-squared Value:", r2)
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)

    try:
        import matplotlib.pyplot as plt
        plt.figure(figsize=(8,6))
        plt.scatter(y_test, y_pred)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
        plt.title("Multiple Linear Regression on Iris Dataset")
        plt.xlabel("Actual Values")
        plt.ylabel("Predicted Values")
        plt.show()
    except Exception as e:
        print("Plotting failed:", e)

if __name__ == '__main__':
    run()
