import pandas as pd

def import_data():
    return pd.read_csv("Liste+d'actions+-+P7+Python+-+Feuille+1.csv", sep="," ,skiprows=1, names=["#", "cost", "return"])

def calculate_roi(action):
    return (int(action["return"].replace("%","")) * action["cost"]) / 100

