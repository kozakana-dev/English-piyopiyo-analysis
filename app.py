import streamlit as st
import google.generativeai as genai
from PIL import Image

# ページ設定
st.set_page_config(page_title="英文解析アプリ")
st.title("英文解析アプリ")

# API設定（バージョン指定を排除）
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# アップロード
uploaded_file = st.file_uploader("画像を選択", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)
    if st.button("解析"):
        try:
            # モデル指定をシンプルにする
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(["添付画像を解析して", image])
            st.write(response.text)
        except Exception as e:
            st.error(f"エラー: {e}")
