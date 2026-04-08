from agents.symptom_extractor import extract_symptoms
from utils.hpo_lookup import search_hpo

def diagnose(patient_description: str):
    print("=" * 50)
    print(f"患者描述：{patient_description}")
    print("=" * 50)

    # 第一步：提取症状
    print("\n【步骤1】提取症状关键词...")
    symptoms = extract_symptoms(patient_description)
    print(f"  → {symptoms}")

    # 第二步：每个症状去HPO里查
    print("\n【步骤2】匹配HPO编码...")
    hpo_results = {}
    for symptom in symptoms:
        matches = search_hpo(symptom)[:3]
        hpo_results[symptom] = matches
        print(f"  '{symptom}' → {[m['code'] + ' ' + m['name'] for m in matches]}")

    print("\n【完成】HPO映射结果：")
    for symptom, matches in hpo_results.items():
        print(f"  {symptom}: {[m['code'] for m in matches]}")

if __name__ == "__main__":
    diagnose("患者出现关节疼痛、发烧、面部皮疹，持续一周")