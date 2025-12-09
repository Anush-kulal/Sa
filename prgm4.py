# Program 4: Central tendency and dispersion measures
# Source: Statistics Lab Program PDF
import pandas as pd
import numpy as np

def run():
    data = pd.DataFrame({'Values': [10,20,20,30,40,50,50,50,60,70]})
    print("Central Tendency Measures")
    mean = np.mean(data['Values'])
    median = np.median(data['Values'])
    mode = data['Values'].mode().iloc[0]
    variance = np.var(data['Values'])
    mean_dev = np.mean(np.abs(data['Values'] - mean))
    q1 = np.percentile(data['Values'], 25)
    q3 = np.percentile(data['Values'], 75)
    quartile_dev = (q3 - q1) / 2

    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)
    print("Variance:", variance)
    print("Mean Deviation:", mean_dev)
    print("Quartile Deviation:", quartile_dev)
    print("\nSummary Statistics:")
    print(data['Values'].describe())

if __name__ == '__main__':
    run()
