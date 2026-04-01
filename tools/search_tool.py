from typing import Dict, Any

def search_attractions(city: str) -> str:
    \"\"\"
    使用 DuckDuckGo 搜尋 `{city} 景點`
    \"\"\"
    # TODO: 實作搜尋邏輯
    return f"（請實作 search_attractions 搜尋 {city} 的景點）"

def search_food(city: str) -> str:
    \"\"\"
    使用 DuckDuckGo 搜尋 `{city} 必吃美食`
    \"\"\"
    # TODO: 實作搜尋邏輯
    return f"（請實作 search_food 搜尋 {city} 的美食）"

def search_outfit(city: str) -> str:
    \"\"\"
    使用 DuckDuckGo 搜尋 `{city} 天氣 穿搭`
    \"\"\"
    # TODO: 實作搜尋邏輯
    return f"（請實作 search_outfit 搜尋 {city} 的穿搭建議）"

TOOL = {
    "name": "search_tool",
    "description": "搜尋當地的熱門景點、美食或天氣穿搭建議。",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "想搜尋的關鍵字"
            }
        },
        "required": ["query"]
    }
}
