import streamlit as st
import google.generativeai as genai
from PIL import Image

st.title("英文解析アプリ")
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# モデル指定の書き方を強制変更
model = genai.GenerativeModel("models/gemini-1.5-flash")

uploaded_file = st.file_uploader("画像を選択", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)
    if st.button("解析実行"):
        try:
            # モデルのgenerate_contentメソッドを直呼び出し
            response = model.generate_content(image)
            st.write(response.text)
        except Exception as e:
            st.error(f"エラー内容: {e}")
