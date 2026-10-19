from dataclass_report import Report
import pandas as pd
import json

def import_data(dataset_name):
    """importe un dataset depuis un CSV, le valide, fait un rapport d'exploration et retourne le dataset validé

    Args:
        dataset_name (str): nom du fichier CSV à importer avec son extension

    Returns:
        pd.DataFrame: le dataset validé
    """
    report = Report()
    report.file_name = dataset_name
    #importation du dataset
    df = pd.read_csv(dataset_name + ".csv", sep="," ,decimal=".",skiprows=1, names=["name", "cost", "performance"],dtype={"cost": float})
        
    # formattage de performance
    df["performance"] = df["performance"].astype(str).str.replace("%","",regex=False).str.strip().astype(float).copy()
    report.validation.all_entries = len(df)
    temp = len(df)
    
    #validation des costs
    df = df[df["cost"] > 0].copy()
    report.validation.invalid_costs = temp - len(df)
    temp = len(df)
    
    #validation des performances
    df = df[df["performance"] > 0].copy()
    report.validation.invalid_performances = temp - len(df)
    temp = len(df)
    
    #suppression des doublons
    df = df.drop_duplicates(subset=["name","cost", "performance"], keep="first").copy()
    df = df.drop_duplicates(subset="name", keep=False).copy()
    report.validation.duplicates = temp - len(df)
    report.validation.valid_entries = len(df)
    
    #calcul du gain
    df["gain"] = ((df["cost"] * df["performance"]) / 100).round(2)
    
    #calcul des statistiques
    for parameter in ("cost","performance","gain"):
        stats = getattr(report.analysis,parameter)
        stats.min = df[parameter].min()
        stats.max = df[parameter].max()
        stats.mean = df[parameter].mean()
        stats.median = df[parameter].median()
        stats.stdev = df[parameter].std()
    
    
    #exportation du report 
    with open("report_" + dataset_name + ".json", "w") as f:
            json.dump(report.to_dict() , f, indent=4)
    
    
    return df.reset_index(drop=True)
