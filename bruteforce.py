from utils import import_data, calculate_roi

data = import_data()
result = []
comb_idx=0
while comb_idx < 2**len(data):
    cost = 0
    roi = 0
    for idx, element in data.iterrows():
        if comb_idx & (1 << idx):
            cost += int(element["cost"])
            roi += int(calculate_roi(element))
    result.append({"combination": comb_idx, "cost": cost, "ROI": roi})
    comb_idx += 1
    print(comb_idx)
result = [r for r in result if r["cost"] <= 500]
result = sorted(result, key=lambda x: x["ROI"], reverse=True)
print(f"Best investment with a cost of {result[0]['cost']}€ and a profit of {result[0]['ROI']}€")
print("Combination of actions:")
for idx, element in data.iterrows():
    if result[0]["combination"] & (1 << idx):
        print(f"- {element['#']} with a cost of {element['cost']}€ and a return of {element['return']}")