import numpy as np

class HealthAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe

    def disease_stats(self):
        disease_amount = self.df["disease"].mean()
        print(f"Antal personer som har sjukdomen:{disease_amount:.2f}")

        simuleringar = [np.random.choice([0, 1], size=1000, p=[1 - disease_amount, disease_amount]).mean() for _ in range(1000)]
        print(f"Medel av 1000 simuleringar: {np.mean(simuleringar):.4f}")
        print(f"Standardavvikelse: {np.std(simuleringar):.4f}")

    def bootstrap_method(self):
        data = self.df["systolic_bp"]
        num_samples = 10_000

        bootstrap_means = np.zeros(num_samples)
        for i in range(num_samples):
            bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
            bootstrap_means[i] = np.mean(bootstrap_sample)
        ci_lower, ci_higher = np.percentile(bootstrap_means, [2.5, 97.5])

        return ci_lower, ci_higher