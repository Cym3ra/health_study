import pandas as pd, numpy as np

def column_stats(df):
    chosen_columns = df[["age", "weight", "height", "systolic_bp", "cholesterol"]]
    statistics_of_columns = pd.DataFrame({"Medel": chosen_columns.mean(), "Median": chosen_columns.median(),
                                      "Min": chosen_columns.min(), "Max": chosen_columns.max()})

    return statistics_of_columns


def hypo_test(df):
    smokers = df[df['smoker']=='Yes']['systolic_bp']
    nonsmokers = df[df['smoker']=='No']['systolic_bp']

    n_boot = 10_000
    obs_diff = smokers.mean() - nonsmokers.mean()

    boot_diffs = np.empty(n_boot)
    for i in range(n_boot):
        A_group = np.random.choice(smokers, size=len(smokers), replace=True)
        B_group = np.random.choice(nonsmokers, size=len(nonsmokers), replace=True)
        boot_diffs[i] = B_group.mean() - A_group.mean()

    p_boot = np.mean(boot_diffs <= 0)

    ci_low, ci_high = np.percentile(boot_diffs, [2.5, 97.5])

    return obs_diff, p_boot, (float((ci_low)), float(ci_high))
