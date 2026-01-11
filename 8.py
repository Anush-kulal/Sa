import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

data = pd.DataFrame({
    "Group": ["A", "B", "C", "A"],
    "Values": [10, 18, 20, 15]
})

print("One-way ANOVA")
groupA = data[data['Group'] == 'A']['Values']
groupB = data[data['Group'] == 'B']['Values']
groupC = data[data['Group'] == 'C']['Values']

f_stat, p_val = stats.f_oneway(groupA, groupB, groupC)
print("F-Statistic:", f_stat)
print("P-Value:", p_val)

if p_val < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")

print("\nTwo-way ANOVA")
data = pd.DataFrame({
    "Group1": ["A", "B", "C", "A"],
    "Group2": ["F", "M", "M", "F"],
    "Values": [10, 18, 20, 15]
})

model = ols('Values ~ C(Group1) + C(Group2) + C(Group1):C(Group2)', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

p_val1 = anova_table.loc["C(Group1)", "PR(>F)"]
p_val2 = anova_table.loc["C(Group2)", "PR(>F)"]

if p_val1 < 0.05 or p_val2 < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")

print("\nTukey HSD Test")
tukey = pairwise_tukeyhsd(endog=data["Values"], groups=data["Group1"], alpha=0.05)
print(tukey)
