import os
import sys
import json
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --- 載入環境變數 ---
load_dotenv()

# --- Import Tools (with fallback mocks) ---
try:
    from tools.weather_tool import get_weather
except ImportError:
    get_weather = lambda city: f"（尚未實作 weather_tool）"

try:
    from tools.search_tool import search_attractions, search_food, search_outfit
except ImportError:
    search_attractions = lambda city: f"（尚未實作 search_tool）"
    search_food = lambda city: f"（尚未實作 search_tool）"
    search_outfit = lambda city: f"（尚未實作 search_tool）"

try:
    from tools.bored_tool import get_random_activity
except ImportError:
    get_random_activity = lambda: "（尚未實作 bored_tool）"

try:
    from tools.trivia_tool import get_random_trivia
except ImportError:
    get_random_trivia = lambda: "（尚未實作 trivia_tool）"

try:
    from tools.advice_tool import get_random_advice
except ImportError:
    get_random_advice = lambda: "（尚未實作 advice_tool）"

def get_llm():
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key or api_key == "your_api_key_here":
            return None
        return ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", 
            temperature=0.7, 
            google_api_key=api_key
        )
    except Exception as e:
        print(f"初始化 Gemini 失敗: {e}")
        return None


def generate_briefing(city: str) -> str:
    """舊版 Markdown 格式（保留相容性）"""
    d = generate_briefing_data(city)
    return f"""
## 🎒 {city} 專屬行前簡報
### 🌤️ 天氣：{d.get('weather', '')}
### 👗 穿搭：{d.get('outfit', '')}
### 📸 景點：{d.get('attractions', '')}
### 🍜 美食：{d.get('food', '')}
### 🎯 活動：{d.get('activity', '')}
### 🧠 冷知識：{d.get('trivia', '')}
### 💬 格言：{d.get('advice', '')}
"""


def generate_briefing_data(city: str) -> dict:
    """
    呼叫所有 Tool 獲取原始資料，並交由 Gemini 將外語內容與生硬的查無資料
    轉換為生動有趣的當地視角繁體中文簡報。
    """
    # 1. 取得原始資料
    raw_weather = get_weather(city)
    raw_attractions = search_attractions(city)
    raw_food = search_food(city)
    raw_outfit = search_outfit(city)
    raw_activity = get_random_activity()
    raw_trivia = get_random_trivia()
    raw_advice = get_random_advice()

    # 2. 如果沒有設定好 LLM 或是 Key 不正確，退回原本直接顯示的行為
    llm = get_llm()
    if not llm:
        print("警告: 尚未設定正確的 GEMINI_API_KEY 或套件安裝失敗，將直接回傳原始資料。")
        return {
            "city": city,
            "weather": raw_weather,
            "attractions": raw_attractions,
            "food": raw_food,
            "outfit": raw_outfit,
            "activity": raw_activity,
            "trivia": raw_trivia,
            "advice": raw_advice,
        }

    prompt = f"""
你是一位簡潔、幽默且專業的當地旅遊嚮導。請根據以下原始資料，為即將前往「{city}」的旅客撰寫一份精簡的行前簡報。

[原始資料]
城市: {city}
天氣: {raw_weather}
景點: {raw_attractions}
美食: {raw_food}
穿搭: {raw_outfit}
活動: {raw_activity}
冷知識: {raw_trivia}
格言: {raw_advice}

[重要規則]
1. 全部使用繁體中文（專有名詞可保留英文）。
2. 每個欄位最多 2~3 句話，保持精簡有力，不要長篇大論。
3. 如果原始資料是英文或很隨機，請巧妙結合「{city}」的在地情境改寫。
4. 如果欄位標註「尚未實作」，請直接推薦 3 項該城市的真實資訊（用短列點）。
5. 調性：親切、有活力、像朋友出發前的叮嚀。

[輸出格式]
回傳純 JSON（不要加 ```json 標記），包含以下 Key：
{{
  "city": "{city}",
  "weather": "簡短天氣摘要",
  "attractions": "3個必去景點（短列點）",
  "food": "3道必吃美食（短列點）",
  "outfit": "簡短穿搭建議",
  "activity": "一項在地化活動建議",
  "trivia": "一則有趣的在地冷知識",
  "advice": "一句旅行格言"
}}
"""

    try:
        response = llm.invoke(prompt)
        content = response.content.strip()
        
        # 簡單清洗可能夾帶的 Markdown JSON 標記
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
            
        final_data = json.loads(content.strip())
        return final_data
    except Exception as e:
        print(f"Gemini API 處理失敗: {e}")
        # 失敗保護：回退回預設資料
        return {
            "city": city,
            "weather": raw_weather,
            "attractions": raw_attractions,
            "food": raw_food,
            "outfit": raw_outfit,
            "activity": raw_activity,
            "trivia": raw_trivia,
            "advice": raw_advice,
        }
