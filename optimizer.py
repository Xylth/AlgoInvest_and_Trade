from utils import import_data
import argparse

BUDGET = 500

#gestion des arguments de la ligne de commande
parser = argparse.ArgumentParser(description="Algo optimisé")
parser.add_argument("dataset_name", help="Nom du fichier de données")
args = parser.parse_args()

#importation du dataset et initialisation de la liste des résultats
data = import_data(args.dataset_name)
data["cost_cents"] = (data["cost"] * 100).round().astype(int)

costline = [{"node_idx" : -1 , "reached" : -1 , "old" : -1} for val in range((BUDGET * 100 )+1)]
nodes = []
empty_node = {
            "cost":0,
            "gain":0,
            "share": 0,
            "cost_cents" : 0
        }
shares_tracker = [{"share_idx":-1 , "previous" : 0}]
nodes.append(empty_node)
costline[0]["node_idx"] = 0
best_node = 0
operation = 0 
new_node = empty_node
for idx, element in data.iterrows():
    old_save = []
    nb_nodes = len(nodes)
    for idx_source_node in range(nb_nodes):
        source_node = nodes[idx_source_node]
        source_costline = costline[source_node["cost_cents"]]
        target_cost = source_node["cost_cents"] + element["cost_cents"]
        
        if target_cost <= BUDGET*100:
            if source_costline["reached"]!= idx:
                new_node = {
                    "cost": target_cost/100 ,
                    "gain":source_node["gain"] + element["gain"],
                    "share": len(shares_tracker),
                    "cost_cents" : target_cost
                } 
                previous_share = source_node["share"]
            else :
                new_node = {
                    "cost": target_cost/100 ,
                    "gain":old_save[source_costline["old"]]["gain"] + element["gain"],
                    "share": len(shares_tracker),
                    "cost_cents" : target_cost
                }
                previous_share = old_save[source_costline["old"]]["share"]     
            if costline[target_cost]["node_idx"]==-1:
                nodes.append(new_node)
                shares_tracker.append({"share_idx":idx , "previous" : previous_share})
                costline[target_cost]["node_idx"]=len(nodes)-1
            else:
                old_node = nodes[costline[target_cost]["node_idx"]]
                old_save.append(old_node)
                costline[target_cost]["old"]=len(old_save)-1
                if (new_node["gain"]>nodes[costline[target_cost]["node_idx"]]["gain"]):
                    nodes[costline[target_cost]["node_idx"]] = new_node
                    shares_tracker.append({"share_idx":idx , "previous" : previous_share})
                costline[target_cost]["reached"] = idx
            if nodes[best_node]["gain"]<new_node["gain"]:
                best_node = costline[new_node["cost_cents"]]["node_idx"]
        operation += 1
        
#affichage de la meilleure combinaison d'actions
print(f"Done in {operation} steps")
print(f"The best investment returns {nodes[best_node]['gain']:.2f}€ with a cost of {nodes[best_node]['cost']}€ for a global performance of {nodes[best_node]['gain']/nodes[best_node]['cost']*100:.2f}%")
print("Combination of actions:")
tracker = shares_tracker[nodes[best_node]["share"]]
while tracker["share_idx"] !=-1:
    share = data.loc[tracker["share_idx"]]
    print(f"- {share['name']} with a cost of {share['cost']}€ and a performance of {share['performance']}% provides a gain of {share['gain']:.2f}€")
    tracker = shares_tracker[tracker["previous"]]
                
            
