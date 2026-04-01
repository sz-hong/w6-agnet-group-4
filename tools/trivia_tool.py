import requests

def get_random_trivia() -> str:
    \"\"\"
    這個函式由負責的組員實作。
    功能：呼叫 https://uselessfacts.jsph.pl/api/v2/facts/random 取得旅遊相關冷知識。
    回傳：一則隨機知識的字串
    \"\"\"
    # TODO: 實作抓取邏輯
    return "（請實作 trivia_tool 呼叫 API 取得冷知識）"

TOOL = {
    "name": "trivia_tool",
    "description": "取得一則隨機的冷知識。",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}
