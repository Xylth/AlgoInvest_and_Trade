from utils import import_data
import argparse

BUDGET = 500

#gestion des arguments de la ligne de commande
parser = argparse.ArgumentParser(description="Algo bruteforce")
parser.add_argument("dataset_name", help="Nom du fichier de données")
args = parser.parse_args()

#importation du dataset et initialisation de la liste des résultats
data = import_data(args.dataset_name)
results = []

#parcours de toutes les combinaisons possibles d'actions de 0 à 2^n-1 (où n est le nombre d'actions)
comb_idx=0
while comb_idx < 2**len(data):
    #initialisation du coût et du gain pour la combinaison actuelle
    cost = 0
    gain = 0
    
    #parcours de toutes les actions pour la combinaison actuelle
    for idx, element in data.iterrows():
        #vérification si l'action est incluse dans la combinaison actuelle (en utilisant un masque binaire)
        if comb_idx & (1 << idx):
            #ajout du coût et du gain de l'action à la combinaison actuelle
            cost += element["cost"]
            gain += element["gain"]
    #ajout de la combinaison actuelle à la liste des résultats
    results.append({"combination": comb_idx, "cost": cost, "gain": gain})
    comb_idx += 1
    print(f"Processing combination {comb_idx} of {2**len(data)}")
    
#filtrage des résultats pour correspondre au budget et tri pour obtenir la combinaison au meilleur gain pour le moindre coût
results = [r for r in results if r["cost"] <= BUDGET]
results = sorted(results, key=lambda x: x["cost"], reverse=False)
results = sorted(results, key=lambda x: x["gain"], reverse=True)

#affichage de la meilleure combinaison d'actions
print(f"The best investment returns {results[0]['gain']:.2f}€ with a cost of {results[0]['cost']}€ for a global preformance of {results[0]['gain']/results[0]['cost']*100:.2f}%")
print("Combination of actions:")
for idx, element in data.iterrows():
    if results[0]["combination"] & (1 << idx):
        print(f"- {element['name']} with a cost of {element['cost']}€ and a performance of {element['performance']}% provides a gain of {element['gain']:.2f}€")
