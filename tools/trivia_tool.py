import requests

def get_random_trivia() -> str:
    """
    這個函式由負責的組員實作。
    功能：呼叫 https://uselessfacts.jsph.pl/api/v2/facts/random 取得旅遊相關冷知識。
    回傳：一則隨機知識的字串
    """
    try:
        response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random", timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("text", "A day on Venus is longer than a year on Venus.")
    except Exception:
        return "The Eiffel Tower can be 15 cm taller during the summer."

TOOL = {
    "name": "trivia_tool",
    "description": "取得一則隨機的冷知識。",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}
