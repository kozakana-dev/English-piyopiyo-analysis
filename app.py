import streamlit as st
import google.generativeai as genai
from PIL import Image

st.title("英文解析アプリ")

# 設定：APIキーのみを読み込む
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# モデル指定：バージョン指定を一切含めない「gemini-1.5-flash」のみにする
model = genai.GenerativeModel("gemini-1.5-flash")

uploaded_file = st.file_uploader("画像を選択", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)
    if st.button("解析実行"):
        try:
            # generate_contentを呼び出す
            response = model.generate_content(image)
            st.write(response.text)
        except Exception as e:
            st.error(f"エラー内容: {e}")
