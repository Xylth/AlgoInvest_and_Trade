import pandas as pd

def import_data(dataset_name):
    return pd.read_csv(dataset_name, sep="," ,decimal=".",skiprows=1, names=["#", "cost", "return"])

def calculate_roi(action):
    return (int(action["return"].replace("%","")) * action["cost"]) / 100

