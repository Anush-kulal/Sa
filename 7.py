import pandas as pd
import numpy as np
from scipy import stats

data = pd.DataFrame({'Values': [12, 15, 14, 16, 18, 20, 22, 19]})
print(data)

print("One Sample T-Test")
print("------------------")
null_mean = 0
t_stat, p_val = stats.ttest_1samp(data['Values'], null_mean)
print("T-Statistic:", t_stat)
print("P-Value:", p_val)

if p_val < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")

print("\nTwo Sample T-Test")
print("------------------")
data1 = [10, 12, 14, 11]
t_stat, p_val = stats.ttest_ind(data['Values'], data1)
print("T-Statistic:", t_stat)
print("P-Value:", p_val)

if p_val < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")

print("\nPaired Sample T-Test")
print("---------------------")
after = [70, 68, 60, 66, 72, 65, 69, 71]
t_stat, p_val = stats.ttest_rel(data['Values'], after)
print("T-Statistic:", t_stat)
print("P-Value:", p_val)

if p_val < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")

print("\nSummary Statistics")
print("---------------------")
print("Sample 1 Mean:", np.mean(data['Values']), " Std Dev:", np.std(data['Values']))
print("Sample 2 Mean:", np.mean(data1), " Std Dev:", np.std(data1))
print("Paired Sample Mean:", np.mean(after), " Std Dev:", np.std(after))
