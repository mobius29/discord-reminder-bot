import requests

def read_notion_db(dbId: str, headers: dict):
    read_url = f"https://api.notion.com/v1/databases/{dbId}/query"
    response = requests.get(read_url, headers=headers)
    
    return response.json()
