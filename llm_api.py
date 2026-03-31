import requests

API_KEY = ""

def ask_llm(symptom_text):
    response = requests.post(
        "https://api.deepseek.com/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "你是一个医疗助手"},
                {"role": "user", "content": f"患者症状：{symptom_text}，可能是什么疾病？"}
            ]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

print(ask_llm("患者出现关节疼痛、皮疹、发烧"))