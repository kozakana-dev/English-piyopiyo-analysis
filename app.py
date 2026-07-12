import streamlit as st
from google import genai
from PIL import Image

# 画面の基本設定
st.set_page_config(page_title="英文SVOC解析アプリ", layout="centered")
st.title("📱 英文 SVOC・文法解析アプリ")

# Secretsからキーを取得
api_key = st.secrets["GOOGLE_API_KEY"]
client = genai.Client(api_key=api_key)

# アップロードエリア
uploaded_file = st.file_uploader("英文の写真を撮るか、画像を選択してください", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="解析対象の画像", use_container_width=True)

    if st.button("✨ 英文を解析する", type="primary"):
        with st.spinner("AIが解析しています..."):
            try:
                prompt = "添付画像から英文を読み取り、SVOC解析と日本語訳、文法解説を行ってください。"
                response = client.models.generate_content(
                    model="gemini-1.5-flash", 
                    contents=[prompt, image]
                )
                st.markdown("### 📚 解析結果")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
