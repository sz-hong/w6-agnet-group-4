from typing import Dict, Any

def get_weather(city: str) -> str:
    \"\"\"
    這個函式由負責的組員實作。
    功能：呼叫 https://wttr.in/{city}?format=j1 API 取得天氣。
    回傳：例如 "溫度：25°C, 天氣：Clear"
    \"\"\"
    # TODO: 實作抓取邏輯
    return f"（請在此處實作 weather_tool 呼叫 API 取得 {city} 天氣）"

TOOL = {
    "name": "weather_tool",
    "description": "查詢目的地的即時天氣",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "要查詢天氣的城市名稱，例如: Tokyo"
            }
        },
        "required": ["city"]
    }
}

if __name__ == '__main__':
    # 可以在此測試
    print(get_weather("Taipei"))
