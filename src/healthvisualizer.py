import matplotlib.pyplot as plt

class HealthVisualizer:
    def __init__(self, dataframe):
        self.df = dataframe

    def plot_hist(self, column, title="", xlabel="", ylabel=""):
        fig, ax = plt.subplots(figsize=(8, 5))
        self.df[column].dropna().plot(kind="hist", bins=20, edgecolor="black", ax=ax)

        ax.set_title(title)
        ax.set_xlabel(xlabel if xlabel else column)
        ax.set_ylabel(ylabel)
        ax.grid(True, axis="y")

        plt.tight_layout()
        plt.show()

    def plot_bar(self, column, title="", xlabel="", ylabel="", normalize=True):
        fig, ax = plt.subplots(figsize=(8, 5))
        self.df[column].value_counts(normalize=normalize).plot(kind="bar", ax=ax)

        ax.set_title(title)
        ax.set_xlabel(xlabel if xlabel else column)
        ax.set_ylabel(ylabel)
        ax.grid(True, axis="y")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=360)
        plt.tight_layout()
        plt.show()

    def plot_scatter(self, x_col, y_col, title="", xlabel="", ylabel=""):
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(self.df[x_col], self.df[y_col])

        ax.set_title(title)
        ax.set_xlabel(xlabel if xlabel else x_col)
        ax.set_ylabel(ylabel if ylabel else y_col)
        ax.grid(True, axis="y")

        plt.tight_layout()
        plt.show()
