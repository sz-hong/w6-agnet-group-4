from typing import Dict, Any
import warnings

# 忽略因為套件改名 (`ddgs`) 而產生的 RuntimeWarning
warnings.filterwarnings("ignore", category=RuntimeWarning, module="duckduckgo_search")

from duckduckgo_search import DDGS

def _perform_search(query: str, max_results: int = 3) -> str:
    """內部共用搜尋邏輯"""
    try:
        results = []
        # 使用 DuckDuckGo 進行文字搜尋
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                title = r.get('title', '')
                body = r.get('body', '')
                results.append(f"- 【{title}】 {body}")
                
        if results:
            return "\n".join(results)
        return f"（目前找不到關於「{query}」的特定資訊）"
    except Exception as e:
        return f"（搜尋「{query}」時發生錯誤，請稍後再試：{e}）"

def search_attractions(city: str) -> str:
    """
    使用 DuckDuckGo 搜尋 `{city} 景點`
    """
    print(f"🔄 正在為您搜尋 {city} 的景點...")
    return _perform_search(f"{city} 必去熱門景點 推薦", max_results=3)

TOOL = {
    "name": "search_tool",
    "description": "搜尋並取得指定城市的熱門景點。",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "想搜尋的城市名稱，例如：Tokyo, Taipei"
            }
        },
        "required": ["city"]
    }
}

if __name__ == '__main__':
    # 測試執行
    print("=== 測試開始 ===")
    test_city = "Kyoto"
    
    print(f"【{test_city} 景點】\n{search_attractions(test_city)}\n")
    print("=== 測試結束 ===")
