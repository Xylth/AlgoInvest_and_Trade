from utils import import_data
import argparse

BUDGET = 500

#gestion des arguments de la ligne de commande
parser = argparse.ArgumentParser(description="Algo bruteforce")
parser.add_argument("dataset_name", help="Nom du fichier de données")
args = parser.parse_args()

#importation du dataset et initialisation de la liste des résultats
data = import_data(args.dataset_name)
results =  [{"idx_share": -1,"cost": 0 ,"gain": 0, "previous":-1}]
n = len(data)
best_comb = results[0]
operation = 0
costs = data["cost"].tolist()
gains = data["gain"].tolist()
names = data["name"].tolist()
performances = data["performance"].tolist()
for idx in range(n):
    cost, gain= costs[idx],gains[idx]
    for previous_idx in range(len(results)):
        result = results[previous_idx]
        new_cost = result["cost"] + cost
        if(new_cost<=BUDGET):
            new_result = {"idx_share" : idx, "cost": new_cost ,"gain": result["gain"] + gain, "previous": previous_idx }
            if((best_comb["gain"]<new_result["gain"]) or ((best_comb["gain"] == new_result["gain"]) and (best_comb["cost"]>new_cost))):
                best_comb = new_result
            results.append(new_result)
        operation += 1
    
#affichage de la meilleure combinaison d'actions

print(f"Done in {operation} steps")
if (best_comb["cost"]>0):
    print(f"The best investment returns {best_comb['gain']:.2f}€ with a cost of {best_comb['cost']:.2f}€ for a global performance of {best_comb['gain']/best_comb['cost']*100:.2f}%")
    print("Combination of actions:")
    idx_share = best_comb["idx_share"]
    previous_idx = best_comb["previous"]
    while idx_share != -1 :
        print(f"- {names[idx_share]} with a cost of {costs[idx_share]:.2f}€ and a performance of {performances[idx_share]:.2f}% provides a gain of {gains[idx_share]:.2f}€")
        idx_share = results[previous_idx]["idx_share"]
        previous_idx = results[previous_idx]["previous"]
else :
    print("No investment possible in the budget")