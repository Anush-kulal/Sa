import matplotlib
matplotlib.use('TkAgg') # Use the TkAgg backend for stable display
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
# Step 1: Generate 100 random values of x in the range [0, 1]
np.random.seed(42) # For reproducibility
x_values = np.random.rand(100, 1) # 100 random values in the range [0,1]
# Step 2: Label the first 50 points as Class1 and the rest as Class2
y_labels = np.array(['Class1' if x <= 0.5 else 'Class2' for x in
x_values.flatten()])
# Split into training and testing sets
X_train = x_values[:50] # First 50 points
y_train = y_labels[:50] # First 50 labels
X_test = x_values[50:] # Remaining 50 points
y_test = y_labels[50:] # Remaining 50 labels
# Step 3: Classify using KNN for different k values
k_values = [1, 2, 3, 4, 5, 20, 30]
plt.figure(figsize=(12, 8))
for i, k in enumerate(k_values, 1):
# Initialize the k-NN classifier with the current k value
knn = KNeighborsClassifier(n_neighbors=k)
# Fit the model on the training data
knn.fit(X_train, y_train)
# Predict the labels for the test set
y_pred = knn.predict(X_test)
# Plot the decision boundary and the points
plt.subplot(3, 3, i)
plt.scatter(X_test, y_test, color='blue', label='True Label')
plt.scatter(X_test, y_pred, color='red', marker='x', label='Predicted Label')
plt.title(f"KNN with k={k}")
plt.xlabel("X value")
plt.ylabel("Class Label")
plt.legend(loc='best')
plt.grid(True)
# Display the plots
plt.tight_layout()
plt.show()
# Step 4: Evaluate classification accuracy for each k value
for k in k_values:
  knn = KNeighborsClassifier(n_neighbors=k)
  knn.fit(X_train, y_train)
  accuracy = knn.score(X_test, y_test)
  print(f"Accuracy for k={k}: {accuracy:.2f}")
