from utils import import_data
import argparse

BUDGET = 500

#gestion des arguments de la ligne de commande
parser = argparse.ArgumentParser(description="Algo optimisé")
parser.add_argument("dataset_name", help="Nom du fichier de données")
args = parser.parse_args()

#importation du dataset et initialisation des variables
data = import_data(args.dataset_name)
data["cost_cents"] = (data["cost"] * 100).round().astype(int)

n = len(data)


total_gain = 0
shares = []
money = BUDGET * 100
best = [0.0] * ((BUDGET*100) +1)
table = [bytearray((BUDGET*100) +1) for _ in range(n)]
costs = data["cost_cents"].tolist()
gains = data["gain"].tolist()

#parcours de toutes les actions
for idx in range(n):
    cost,gain,line = costs[idx], gains[idx], table[idx]
    
    #parcours de toutes les valeurs en centimes
    for step in range(BUDGET*100, cost - 1,-1):
        new_val = best[step-cost]+gain
        if new_val>best[step]:
            best[step]=new_val
            line[step] = 1

#determination du gain max et du cost min
gain_max = best[BUDGET*100]
while((money>0) and (best[money-1]==gain_max)):
    money-=1
total_cost = money / 100

#recupération des actions sélectionnées
for idx in range (n-1,-1,-1):
    if(money<=0):
        break
    if(table[idx][money]==1):
        total_gain += gains[idx]
        shares.append(idx)
        money -= costs[idx]

#affichage de la solution
if(total_cost>0):
    print(f"The best investment returns {total_gain:.2f}€ with a cost of {total_cost:.2f}€ for a global performance of {total_gain/total_cost*100:.2f}%")
    print("Combination of actions:")
    for share in data.iloc[shares].itertuples():
        print(f"- {share.name} with a cost of {share.cost}€ and a performance of {share.performance}% provides a gain of {share.gain:.2f}€")
else:
    print("No investment possible in the budget")