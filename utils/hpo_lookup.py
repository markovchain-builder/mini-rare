import json

# 启动时加载一次，不要每次调用都重新读文件
with open("hp.json", "r", encoding="utf-8") as f:
    hp_data = json.load(f)

nodes = hp_data["graphs"][0]["nodes"]


def search_hpo(keyword: str) -> list:
    """
    输入：英文症状关键词，比如 "fever"
    输出：匹配的HPO条目列表，每个是dict，包含name和code
    
    例：search_hpo("fever") 
    → [{"name": "Fever", "code": "HP:0001945"}, ...]
    """
    keyword_lower = keyword.lower()
    results = []

    for node in nodes:
        lbl = node.get("lbl")
        if lbl is None:
            continue

        # 检查主名称是否包含关键词
        name_match = keyword_lower in lbl.lower()
        # 反向检查关键词是否包含主名称
        reverse_match = lbl.lower() in keyword_lower
        # 检查同义词里是否包含关键词
        synonym_match = False
        synonyms = node.get("meta", {}).get("synonyms", [])
        for syn in synonyms:
            if keyword_lower in syn.get("val", "").lower():
                synonym_match = True
                break

        if name_match or reverse_match or synonym_match:
            raw_id = node.get("id", "")
            code = raw_id.replace(
                "http://purl.obolibrary.org/obo/HP_", "HP:"
            )
            results.append({
                "name": lbl,
                "code": code
            })

    return results


def get_hpo_definition(code: str) -> str:
    """
    输入：HPO编码，比如 "HP:0001945"
    输出：该条目的英文定义（没有则返回空字符串）
    """
    raw_id = code.replace("HP:", "http://purl.obolibrary.org/obo/HP_")

    for node in nodes:
        if node.get("id") == raw_id:
            definition = node.get("meta", {}).get("definition", {}).get("val", "")
            return definition

    return ""


# 测试
if __name__ == "__main__":
    print("=== 搜索 fever ===")
    results = search_hpo("fever")
    for r in results[:5]:  # 只打印前5个
        print(r)

    print("\n=== 搜索 joint pain ===")
    results2 = search_hpo("joint pain")
    for r in results2[:5]:
        print(r)

    print("\n=== 获取定义 ===")
    if results:
        code = results[0]["code"]
        print(f"{code} 的定义：{get_hpo_definition(code)}")