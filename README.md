# AI agent 開發分組實作

> 課程：AI agent 開發 — Tool 與 Skill
> 主題： 旅遊前哨站

---

## Agent 功能總覽

> 這個 Agent 是一個「旅遊前哨站」，它可以協助使用者在出發前取得目的地的全方位資訊。使用者只需輸入想去的城市，我們的預處理 Tools 將抓取所有必要的 API，並交給 **Gemini 大模型** 進行在地化翻譯、潤飾與統整，最後於網頁端呈現一份流暢的中文行前簡報。

| 使用者輸入   | Agent 行為                             | 負責組員 |
| ------------ | -------------------------------------- | -------- |
| （例：天氣） | 呼叫 weather_tool，查詢即時天氣        |   陳柏宇 |
| （例：景點） | 呼叫 search_tool，搜尋熱門景點與美食   |   楊承軒   |
| （例：建議） | 呼叫 advice_tool，取得隨機旅行建議     |     陳婉榕     |
| （例：活動） | 呼叫 bored_tool，取得打發時間的活動    |     陳婉榕     |
| （例：知識） | 呼叫 trivia_tool，取得旅遊冷知識       |     陳婉榕     |
| （大腦綜合） | 送入 Gemini 模型進行翻譯與在地化推薦   | 洪紹禎 |
| （前端顯示） | 透過 Flask API 渲染至專屬網頁介面      | 洪紹禎 |

---

## 組員與分工

| 姓名 | 負責功能           | 檔案                  | 使用的技術 / API                       |
| ---- | ----------------- | --------------------- | ------------------------------------ |
| 陳柏宇 | weather_tool      | `tools/weather_tool.py` | `wttr.in`                          |
| 楊承軒 | search_tool       | `tools/search_tool.py`  | DuckDuckGo Search API                |
| 陳婉榕 | bored/trivia/advice | `tools/*.py`          | Bored/UselessFacts/Advice API        |
| 洪紹禎 | Skill 整合 / AI    | `skills/trip_briefing.py`| Gemini 2.5 Flash (`langchain-google-genai`) |
| 洪紹禎 | Agent 後端與前端 UI| `main.py`, `templates/`| Flask + Vanilla HTML/CSS/JS          |

---

## 專案架構

```text
├── tools/
│   ├── instructions.md     # 給各小組成員的實作規範說明
│   ├── weather_tool.py
│   ├── search_tool.py
│   ├── bored_tool.py
│   ├── trivia_tool.py
│   └── advice_tool.py
├── skills/
│   └── trip_briefing.py    # 組合各個工具產出 JSON，並交給 Gemini 潤飾
├── templates/
│   └── index.html          # Web 前端介面（純 HTML/CSS/JS 實作質感介面）
├── main.py                 # Flask 後端應用程式與 API 端點
├── .env.sample             # Gemini API Key 環境變數範本
├── requirements.txt        # 專案相依套件清單 (flask, langchain, google-genai...)
└── README.md
```

---

## 使用方式

請開啟終端機，執行以下指令：

```bash
# 1. 建立並啟動虛擬環境 (Windows 請執行: .venv\Scripts\activate)
python -m venv .venv
source .venv/bin/activate

# 2. 安裝套件
pip install -r requirements.txt

# 3. 設定 API Key
# 請將 .env.sample 複製一份並重新命名為 .env，然後填寫你的 GEMINI_API_KEY
cp .env.sample .env

# 4. 執行 Web App
python main.py
```

> 🔔 啟動後，請開啟瀏覽器前往：`http://127.0.0.1:5000` 即可開始使用！

---

## 執行結果

> 實際的「旅遊前哨站」行前簡報生成畫面（結合了所有 API 工具、並由 Gemini 2.5 潤飾後端資料、且具備全新的前端質感設計）：

**網頁首頁介面**
![首頁設計](assets/homepage.png)

**填入城市（如：Paris) 後產生的精美簡報卡片**
![執行結果卡片](assets/paris_results.png)

---

## 各功能說明

### 天氣查詢（負責：陳柏宇）

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

### 景點與美食搜尋（負責：楊承軒）

- **Tool 名稱**：search_tool
- **使用 API**：`duckduckgo-search` 套件
- **輸入**：搜尋關鍵字（例如 "{city} 景點", "{city} 必吃美食"）
- **輸出範例**：`[{ "title": "...", "href": "...", "body": "..." }]`

### 活動與建議（負責：陳婉榕）

- **Tool 名稱**：bored_tool / trivia_tool / advice_tool
- **使用 API**：Bored API, UselessFacts API, Advice Slip API
- **輸入**：無（或簡單參數）
- **輸出範例**：傳回字串或字典，例如：`"Learn how to write in shorthand. (類型: education)"`

### Skill：行前簡報整合（負責：洪紹禎）

- **組合了哪些 Tool**：`weather_tool`, `search_tool`, `bored_tool`, `trivia_tool`, `advice_tool`
- **執行順序**：

```
Step 1: 呼叫 weather_tool / search_tool / 其它額外 API 工具，取得原始資料（包含英文）。
Step 2: 將全部收集到的純文字/JSON 組合進 Prompt 中。
Step 3: 呼叫 Gemini 2.5 Flash 語言模型，要求模型擔任導遊，翻譯並將隨機資料在地化（例如隨機出現「參觀博物館」，Gemini 會包裝為「去羅浮宮走走」）。
Step 4: 規定 Gemini 輸出指定格式的 JSON 字典，供前端網頁逐區塊展開渲染。
```

---

## 心得

### 遇到最難的問題

> 寫下這次實作遇到最困難的事，以及怎麼解決的

### Tool 和 Skill 的差別

> 用自己的話說說，做完後你怎麼理解兩者的不同

### 如果再加一個功能

> 如果可以多加一個 Tool，你會加什麼？為什麼？
