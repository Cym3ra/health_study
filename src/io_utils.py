import pandas as pd

def load_data(filepath):
    """
    Läser CSV fil
    """
    df = pd.read_csv(filepath)
    return df