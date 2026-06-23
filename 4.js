import pandas as pd

dataset = {
    'Sky': ['Suny', 'Suny', 'Rainy', 'Suny'],
    'AirTemp': ['Warm', 'Cold', 'Warm', 'Warm'],
    'Humidity': ['High', 'Normal', 'High', 'High'],
    'Wind': ['Strong', 'Strong', 'Medium', 'Strong'],
    'Water': ['Warm', 'Warm', 'Warm', 'Cool'],
    'Output': ['Yes', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(dataset)

def find_s(df):
    X = df.iloc[:, :-1].values  # All rows, all columns except the last one
    Y = df.iloc[:, -1].values   # All rows, only the last column (Yes/No)

    for i in range(len(Y)):
        if Y[i] == "Yes":
            h = X[i].copy()    # 'h' is your specific hypothesis tracker
            break

    for i in range(len(Y)):
        if Y[i] == "Yes":
            for j in range(len(h)):
                # If the feature doesn't match our current hypothesis, generalize it
                if h[j] != X[i][j]:
                    h[j] = "?"  # '?' means it accepts any value

    return h

# 3. Run and print
result = find_s(df)
print("Most Specific Hypothesis:", result)
