# Program 7: One-sample, two-sample and paired-sample t-tests
# Source: Statistics Lab Program PDF
import numpy as np
import pandas as pd
from scipy import stats

def run():
    # Example data (replace with your own or load from CSV)
    data = pd.DataFrame({'Values': [10,12,11,13,12,14,15,11,13,12]})
    print("One Sample T-Test")
    null_mean = 0
    t_stat, p_val = stats.ttest_1samp(data['Values'], null_mean)
    print("T-Statistic:", t_stat, "P-Value:", p_val)
    if p_val < 0.05:
        print("Reject null hypothesis")
    else:
        print("Fail to reject null hypothesis")

    # Two-sample t-test example
    data1 = [10, 12, 14, 11]
    t_stat, p_val = stats.ttest_ind(data['Values'], data1, equal_var=False)
    print("\\nTwo-sample T-Test:", "T-Statistic:", t_stat, "P-Value:", p_val)

    # Paired sample t-test example (before vs after)
    after = [70,68,60,66,65,64,63,62,61,60]
    # adjust lengths if needed
    min_len = min(len(data['Values']), len(after))
    t_stat, p_val = stats.ttest_rel(data['Values'][:min_len], after[:min_len])
    print("\\nPaired-sample T-Test:", "T-Statistic:", t_stat, "P-Value:", p_val)

if __name__ == '__main__':
    run()
