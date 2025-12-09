# Program 8: One-way and Two-way ANOVA
# Source: Statistics Lab Program PDF
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def run():
    data = pd.DataFrame({"Group": ["A","B","C","A"], "Values":[10,18,20,15]})
    print("One-way ANOVA")
    groupA = data[data['Group']=='A']['Values']
    groupB = data[data['Group']=='B']['Values']
    groupC = data[data['Group']=='C']['Values']
    f_stat, p_val = stats.f_oneway(groupA, groupB, groupC)
    print("F-Statistic:", f_stat, "P-Value:", p_val)

    data2 = pd.DataFrame({"Group1":["A","B","C","A"], "Group2":["F","M","M","F"], "Values":[10,18,20,15]})
    model = ols('Values ~ C(Group1) + C(Group2) + C(Group1):C(Group2)', data=data2).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    print("\\nTwo-way ANOVA result:\\n", anova_table)

    print("\\nTukey's HSD Test")
    tukey = pairwise_tukeyhsd(endog=data2["Values"], groups=data2["Group1"], alpha=0.05)
    print(tukey)

if __name__ == '__main__':
    run()
