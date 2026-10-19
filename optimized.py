from utils import import_data
import argparse

BUDGET = 500

#gestion des arguments de la ligne de commande
parser = argparse.ArgumentParser(description="Algo optimisé")
parser.add_argument("dataset_name", help="Nom du fichier de données")
args = parser.parse_args()

#importation du dataset et initialisation de la liste des résultats
data = import_data(args.dataset_name)

costline = [-1] * ((BUDGET * 100 )+1)
nodes = []
empty_node = {
            "cost":0,
            "gain":0,
            "shares": []
        }
nodes.append(empty_node)
costline[0] = 0
best_node = 0
operation = 0 
new_node = empty_node
for idx, element in data.iterrows():
    for cursor in range(len(costline)-1, -1, -1):
        if costline[cursor] != -1:
            target_cost = cursor + int(element["cost"]*100)
            if target_cost <= BUDGET*100:
                new_node = {
                    "cost": target_cost/100 ,
                    "gain":nodes[costline[cursor]]["gain"] + element["gain"],
                    "shares": nodes[costline[cursor]]["shares"] + [idx]
                } 
                if costline[target_cost]==-1:
                    nodes.append(new_node)
                    costline[target_cost]=len(nodes)-1
                else:
                    if new_node["gain"]>nodes[costline[target_cost]]["gain"]:
                        nodes[costline[target_cost]]=new_node
                if nodes[best_node]["gain"]<new_node["gain"]:
                    best_node = costline[int(new_node["cost"]*100)]
        operation += 1
        
        

#affichage de la meilleure combinaison d'actions
print(f"The best investment returns {nodes[best_node]['gain']:.2f}€ with a cost of {nodes[best_node]['cost']}€ for a global performance of {nodes[best_node]['gain']/nodes[best_node]['cost']*100:.2f}%")
print("Combination of actions:")
for share in nodes[best_node]["shares"]:
    print(f"- {data.loc[share]['name']} with a cost of {data.loc[share]['cost']}€ and a performance of {data.loc[share]['performance']}% provides a gain of {data.loc[share]['gain']:.2f}€")

                
            
    
