# Tool 開發說明書

各位團隊成員好，此專案我們將共同開發「旅遊前哨站」Agent。為確保彼此的程式碼能夠整合，請依照以下格式與規範進行開發。

## 團隊分工與負責檔案
目前總共有以下幾個主要 Tool 需要實作，請大家自行認領：
1. **即時天氣查詢 (weather_tool.py)**：輸入城市，解析 `temp_C` 與 `weatherDesc`。API：`https://wttr.in/{city}?format=j1`
2. **景點與美食搜尋 (search_tool.py)**：使用 DuckDuckGo 進行網路搜尋（可直接使用 `duckduckgo-search` 套件），搜尋關鍵字例如 "{city} 景點"、"{city} 必吃美食" 或 "{city} 天氣 穿搭"。
3. **無聊活動建議 (bored_tool.py)**：回傳一則活動名稱與類型。API：`https://bored-api.appbrewery.com/random`
4. **旅遊冷知識 (trivia_tool.py)**：回傳隨機的有趣知識。API：`https://uselessfacts.jsph.pl/api/v2/facts/random`
5. **人生格言建議 (advice_tool.py)**：回傳一句隨機建議。API：`https://api.adviceslip.com/advice`

---

## Tool 實作格式規範

每位成員在開發自己的 `.py` 檔案時，請必須包含兩個主要部分：
1. **執行函式**：實際進行 API 呼叫或搜尋的 Python Function。
2. **Tool 描述字典 (TOOL Dictionary)**：定義給 Agent 看的工具說明與參數格式（JSON Schema 格式）。

### 範例格式：`tools/example_tool.py`

```python
import requests

# 1. 實際的執行函式
def get_example_data(city: str) -> dict:
    '''這是一個範例函式，開發者在這裡寫取資料的邏輯'''
    try:
        # 實作你的 API 請求
        # response = requests.get(f"你的API網址/{city}")
        # return response.json()
        return {"city": city, "data": "範例資料"}
    except Exception as e:
        return {"error": str(e)}

# 2. 定義給 Agent / LLM 看的工具介面
TOOL = {
    "name": "example_tool",
    "description": "這是一個範例工具，用於取得某城市的範例資料",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "要查詢的城市名稱，例如：Tokyo, Taipei"
            }
        },
        "required": ["city"]
    }
}
```

## 注意事項
- **Return Type**: 你的函式請一律回傳 `dict` (字典) 或是 `str` (字串)，請確保若是遇到錯誤也要能捕捉 `Exception` 並回傳錯誤訊息字串，避免主程式 Crash。
- **Dependencies**: 若有使用到新的第三方套件，請記得在群組提出並加入根目錄的 `requirements.txt`。
- 完成後，可在自己的檔案內加入 `if __name__ == '__main__':` 進行單一檔案的測試。
