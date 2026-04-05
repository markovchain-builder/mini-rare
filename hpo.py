import pandas as pd
import json
with open("hp.json", "r", encoding="utf-8") as f:
    hp_data = json.load(f)
nodes= hp_data["graphs"][0]["nodes"]
for node in nodes:
    syn=node.get("lbl")
    hpo_name=node.get("id")

    if syn is not None and syn.upper()=="FEVER":
        print("找到发烧")
        print("症状名：", syn)
        print("原始ID：", hpo_name)

        code_id=hpo_name.replace("http://purl.obolibrary.org/obo/HP_","HP:")
        print("标准编码：", code_id)
        break