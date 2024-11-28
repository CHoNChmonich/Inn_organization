import requests

DADATA_API_KEY = "12fef0e47fa948c41d8ea8ab920db4b7839f0016"  # Вставьте API-ключ
DADATA_URL = "https://dadata.ru/api/v2/findById/party"

def fetch_organization_by_inn(inn):
    headers = {
        "Authorization": f"Token {DADATA_API_KEY}",
        "Content-Type": "application/json",
    }
    response = requests.post(DADATA_URL, headers=headers, json={"query": inn})
    if response.status_code == 200:
        data = response.json()
        if data.get("suggestions"):
            return data["suggestions"][0]["data"]
    return None
