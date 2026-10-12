from utils import import_data, calculate_roi

data = import_data()

result = []
node = {"cout": 0, "profit": 0, "combination": []}
result.append(node)
for idx, element in data.iterrows():
    new_nodes = []
    for node in result:
        if node["cout"] + int(element["cost"]) <= 500:
            new_node = {"cout": node["cout"] + int(element["cost"]),
                        "profit": node["profit"] + int(calculate_roi(element)),
                        "combination": node["combination"] + [element["#"]]}
            new_nodes.append(new_node)
    for new_node in new_nodes:
        for idx, existing_node in enumerate(result):
            if new_node["cout"] == existing_node["cout"]:
                result.remove(existing_node)
                if new_node["profit"] < existing_node["profit"]:
                    new_node = existing_node
                    break
        result.append(new_node)
    result = sorted(result, key=lambda x: x["cout"])
result = sorted(result, key=lambda x: x["profit"], reverse=True)
print(f"Best investment with a cost of {result[0]['cout']}€ and a profit of {result[0]['profit']}€")
print("Combination of actions:")
print(result[0]["combination"])