import os
import sys

# 將工具路徑加入環境
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 嘗試匯入各個負責人開發的 Tool，若尚未開發完成則使用 Mock 功能提供暫時的防呆設計
try:
    from tools.weather_tool import get_weather
except ImportError:
    get_weather = lambda city: f"（尚未實作 weather_tool 取得 {city} 的天氣）"

try:
    from tools.search_tool import search_attractions, search_food, search_outfit
except ImportError:
    search_attractions = lambda city: f"（尚未實作 search_tool 取得 {city} 的景點）"
    search_food = lambda city: f"（尚未實作 search_tool 取得 {city} 的美食）"
    search_outfit = lambda city: f"（尚未實作 search_tool 取得 {city} 的穿搭建議）"

try:
    from tools.bored_tool import get_random_activity
except ImportError:
    get_random_activity = lambda: "（尚未實作 bored_tool 取得隨機活動）"

try:
    from tools.trivia_tool import get_random_trivia
except ImportError:
    get_random_trivia = lambda city: "（尚未實作 trivia_tool 取得冷知識）"

try:
    from tools.advice_tool import get_random_advice
except ImportError:
    get_random_advice = lambda: "（尚未實作 advice_tool 取得人生格言）"


def generate_briefing(city: str) -> str:
    """
    這是行前簡報整合 Skill：負責呼叫各個底層 Tool 並將資訊整合成漂亮的 Markdown 格式回傳。
    """
    
    # 執行各個 Tools
    weather_info = get_weather(city)
    attractions_info = search_attractions(city)
    food_info = search_food(city)
    outfit_info = search_outfit(city)
    
    activity = get_random_activity()
    trivia = get_random_trivia(city)
    advice = get_random_advice()
    
    # 組合 Markdown 字串
    briefing = f"""
## 🎒 {city} 專屬行前簡報

---

### 🌤️ 即時天氣與穿搭
- **天氣狀況**：
  > {weather_info}
- **穿搭建議**：
  > {outfit_info}

### 📸 熱門景點與美食
- **必去熱門景點**：
  > {attractions_info}
- **當地必吃美食**：
  > {food_info}

### 💡 旅途小彩蛋
- **無聊時可以找事做**：
  > {activity}
- **當地旅遊冷知識**：
  > {trivia}
- **出發前的人生格言**：
  > _{advice}_

---
✨ **祝您有一趟美好的旅程！** ✨
    """
    
    return briefing
