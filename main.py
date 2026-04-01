import streamlit as st
import time
from skills.trip_briefing import generate_briefing

# 設定網頁設定 (Page config)
st.set_page_config(
    page_title="旅遊前哨站 Agent",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# 載入自訂 CSS 進行美化 (符合 UI/UX 要求)
st.markdown("""
<style>
    /* 這裡可以加入更多的 CSS 樣式美化 UI */
    .report-container {
        padding: 2rem;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        color: #333333;
    }
</style>
""", unsafe_allow_html=True)

st.title("✈️ 旅遊前哨站 Agent")
st.markdown("### 準備好踏上旅程了嗎？\n只要輸入你想去的城市，我們就會整合各種資訊，為你產生專屬出發前的**行前簡報**！")

st.divider()

# 側邊欄供設定 (預設保留未來可放入 API key 或 Model 切換)
with st.sidebar:
    st.header("⚙️ 設定區")
    st.info("這裡可以預留輸入 API Key (如 Gemini, OpenAI) 的欄位。目前實作只需使用公開 API，無須填寫。")

# 主畫面 Input
city_input = st.text_input("輸入你想去的地點（例如：Tokyo, Tainan, Paris）：", placeholder="例如：Taipei")

if st.button("🚀 產生行前簡報", use_container_width=True):
    if not city_input.strip():
        st.warning("請先輸入城市名稱！")
    else:
        with st.spinner(f"正在為您整理 {city_input} 的情報，請稍候... (組合多個 API Tool 中)"):
            try:
                # 模擬等待或實際呼叫的延遲
                time.sleep(1)
                
                # 呼叫 Skill 來產生跨 Tool 組合後的簡報
                report_markdown = generate_briefing(city_input)
                
                st.success("簡報產生完成！🎉")
                
                # 顯示結果
                st.markdown("<div class='report-container'>", unsafe_allow_html=True)
                st.markdown(report_markdown)
                st.markdown("</div>", unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"產生簡報時發生錯誤：{str(e)}")
