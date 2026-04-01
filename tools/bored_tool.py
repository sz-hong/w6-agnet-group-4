import requests

def get_random_activity() -> str:
    """
    這個函式由負責的組員實作。
    功能：呼叫 https://bored-api.appbrewery.com/random API 取得活動建議。
    回傳：回傳活動名稱與類型 (例如：Learn a new recipe (類型: education))
    """
    # TODO: 實作抓取邏輯
    return "（請實作 bored_tool 呼叫 API 取得隨機活動）"

TOOL = {
    "name": "bored_tool",
    "description": "取得一則隨機的休閒活動建議，適合旅途中不知道做什麼時參考。",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}
