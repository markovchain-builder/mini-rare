import requests
import json
API_KEY="your_keys"
def extract_symptoms(patient_description: str) -> list:
    """Input: patients's description in Chinese
       Output:keywords of symptoms in english
       例：
       输入："患者出现关节疼痛、发烧、面部皮疹"
       输出：["joint pain", "fever", "rash"]
    """
    response = requests.post(
        "https://api.deepseek.com/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": "deepseek-chat",
            "messages": [
                {
                    "role": "system",
                    "content": "你是医疗信息提取助手。只输出JSON列表，不输出任何其他文字。"
                },
                {
                    "role": "user",
                    "content": f"""
从下面的患者描述中提取所有症状，翻译成英文关键词。
只输出JSON列表，格式：["symptom1", "symptom2"]
患者描述：{patient_description}
"""
                }
            ]
        }
    )
    raw_text = response.json()["choices"][0]["message"]["content"].strip()
    
    # 清理AI可能加的```json标记
    if raw_text.startswith("```"):
        raw_text = raw_text.split("\n", 1)[-1]
        raw_text = raw_text.rsplit("```", 1)[0]

    return json.loads(raw_text)
   

if __name__ == "__main__":
    result = extract_symptoms("患者出现关节疼痛、发烧、面部皮疹，持续一周")
    print(result)

#有一个还是有点问题 hpo中只有rash 但是实际上的症状描述为 "facial rash"