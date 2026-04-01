import requests

def get_random_advice() -> str:
    \"\"\"
    這個函式由負責的組員實作。
    功能：呼叫 https://api.adviceslip.com/advice 取得旅行格言/人生建議。
    回傳：一句隨機建議字串。
    \"\"\"
    # TODO: 實作抓取邏輯
    return "（請實作 advice_tool 呼叫 API 取得隨機建議）"

TOOL = {
    "name": "advice_tool",
    "description": "取得一則隨機的人生建議或格言。",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}
