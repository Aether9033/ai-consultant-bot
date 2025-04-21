import streamlit as st
import random

st.set_page_config(page_title="AI 商業顧問", page_icon="💼")
st.title("💼 AI 商業顧問")
st.write("請輸入你的問題，我將提供專業建議。輸入 'bye' 結束對話。\n")

advice = {
    "創業": [
        "建議你撰寫簡易商業計畫書，包含產品、客群與資金來源。",
        "請先確認你的商業模式是否有明確價值主張。",
        "創業初期請保守預估成本，並準備至少六個月現金流。"
    ],
    "行銷": [
        "從社群媒體、口碑行銷、合作聯盟三個方向開始切入。",
        "區分目標客群，再針對性設計訊息，有效提升轉換率。",
        "前期可用低成本的數位廣告測試市場反應。"
    ],
    "投資": [
        "請評估你的風險承受度，保守型可考慮 ETF 或定存。",
        "建議你分散投資，不要集中資金在單一標的。",
        "高報酬投資需搭配良好資訊來源與停損機制。"
    ],
    "離職": [
        "建議先做好財務準備與市場驗證，再考慮辭職創業。",
        "可從副業或小規模測試開始，會比直接離職穩健。",
        "離職後的職涯空窗與保險安排，也要列入考量。"
    ]
}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("你：")

if user_input:
    st.session_state.chat_history.append(("你", user_input))

    if user_input.lower() == "bye":
        st.session_state.chat_history.append(("AI 顧問", "感謝你的信任，祝你事業順利！👋"))
    else:
        found = False
        for keyword in advice:
            if keyword in user_input:
                response = random.choice(advice[keyword])
                st.session_state.chat_history.append(("AI 顧問", response))
                found = True
                break
        if not found:
            st.session_state.chat_history.append(("AI 顧問", "這個主題我還在學習中，但建議你先釐清目標與限制條件。"))

for speaker, message in st.session_state.chat_history:
    st.markdown(f"**{speaker}：** {message}")
