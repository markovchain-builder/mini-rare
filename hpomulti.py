import json

with open("hp.json", "r", encoding="utf-8") as f:
    hp_data = json.load(f)

nodes = hp_data["graphs"][0]["nodes"]

for i, node in enumerate(nodes[:3]):
    print(f"=== node {i} ===")
    print(node)
    print()