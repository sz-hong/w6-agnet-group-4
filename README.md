# AI agent 開發分組實作

> 課程：AI agent 開發 — Tool 與 Skill
> 主題： 旅遊前哨站 / 偵探事務所 / 生活顧問

---

## Agent 功能總覽

> 這個 Agent 是一個「旅遊前哨站」，它可以協助使用者在出發前取得目的地的全方位資訊。使用者只需輸入想去的城市，即可取得一份包含天氣、穿搭、景點、美食與旅遊建議的完整行前簡報。

| 使用者輸入   | Agent 行為                             | 負責組員 |
| ------------ | -------------------------------------- | -------- |
| （例：天氣） | 呼叫 weather_tool，查詢即時天氣        |          |
| （例：景點） | 呼叫 search_tool，搜尋熱門景點與美食   |          |
| （例：建議） | 呼叫 advice_tool，取得隨機旅行建議     |          |
| （例：活動） | 呼叫 bored_tool，取得打發時間的活動    |          |
| （例：知識） | 呼叫 trivia_tool，取得旅遊冷知識       |          |
| （例：出發） | 執行 trip_briefing Skill，產出行前簡報 |          |

---

## 組員與分工

| 姓名 | 負責功能           | 檔案                  | 使用的 API                           |
| ---- | ----------------- | --------------------- | ------------------------------------ |
|      | weather_tool      | `tools/weather_tool.py` | `wttr.in`                          |
|      | search_tool       | `tools/search_tool.py`  | DuckDuckGo Search API                |
|      | bored/trivia/advice | `tools/*.py`          | Bored/UselessFacts/Advice API        |
|      | Skill 整合         | `skills/trip_briefing.py` | —                                    |
|      | Agent 主程式       | `main.py`             | Streamlit Web UI                     |

---

## 專案架構

```
├── tools/
│   ├── instructions.md     # 給各小組成員的實作規範說明
│   ├── weather_tool.py
│   ├── search_tool.py
│   ├── bored_tool.py
│   ├── trivia_tool.py
│   └── advice_tool.py
├── skills/
│   └── trip_briefing.py    # 組合各個工具產出行前簡報的邏輯
├── main.py                 # Streamlit Web UI 主程式
├── requirements.txt        # 專案相依套件清單
└── README.md
```

---

## 使用方式

請開啟終端機，執行以下指令：

```bash
# 建立虛擬環境
python3 -m venv .venv

# 啟動虛擬環境 (Windows 請執行: .venv\Scripts\activate)
source .venv/bin/activate

# 安裝套件
pip install -r requirements.txt

# 執行 Web App
streamlit run main.py
```

---

## 執行結果

> 貼上程式執行的實際範例輸出

```
（貼上執行結果，例如下的指令與輸出結果）
```

---

## 各功能說明

### 天氣查詢（負責：姓名）

- **Tool 名稱**：weather_tool
- **使用 API**：`https://wttr.in/{city}?format=j1`
- **輸入**：城市名稱 `{city}`
- **輸出範例**：`{"temp_C": "25", "weatherDesc": "Clear"}`

```python
TOOL = {
    "name": "weather_tool",
    "description": "查詢目的地的即時天氣",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "要查詢天氣的城市名稱"}
        },
        "required": ["city"]
    }
}
```

### 景點與美食搜尋（負責：姓名）

- **Tool 名稱**：search_tool
- **使用 API**：`duckduckgo-search` 套件
- **輸入**：搜尋關鍵字（例如 "{city} 景點", "{city} 必吃美食"）
- **輸出範例**：`[{ "title": "...", "href": "...", "body": "..." }]`

### 活動與建議（負責：姓名）

- **Tool 名稱**：bored_tool / trivia_tool / advice_tool
- **使用 API**：Bored API, UselessFacts API, Advice Slip API
- **輸入**：無（或簡單參數）
- **輸出範例**：傳回字串或字典，例如：`"Learn how to write in shorthand. (類型: education)"`

### Skill：行前簡報整合（負責：姓名）

- **組合了哪些 Tool**：`weather_tool`, `search_tool`, `bored_tool`, `trivia_tool`, `advice_tool`
- **執行順序**：

```
Step 1: 呼叫 weather_tool → 取得天氣資訊
Step 2: 呼叫 search_tool  → 取得景點、美食建議與穿搭建議
Step 3: 呼叫其它 API 工具 → 取得當地活動、冷知識與旅行格言
Step 4: 組合上述所有輸出 → 產生一份完整的 markdown 「行前簡報」並傳回
```

---

## 心得

### 遇到最難的問題

> 寫下這次實作遇到最困難的事，以及怎麼解決的

### Tool 和 Skill 的差別

> 用自己的話說說，做完後你怎麼理解兩者的不同

### 如果再加一個功能

> 如果可以多加一個 Tool，你會加什麼？為什麼？
