import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# APIキーを設定 (⚠️ あなたのキーに書き換えてください)
genai.configure(api_key="")

st.title("英語構文解析カメラ")

# 入力方法の選択（テキストかカメラか）
input_method = st.radio("解析方法を選んでください", ("テキスト入力", "カメラで撮影"))

if input_method == "テキスト入力":
    user_text = st.text_input("解析したい英文を入力してください")
    submit_btn = st.button("テキストを解析")
    image_data = None

else: # カメラで撮影
    camera_image = st.camera_input("英文を撮影してください")
    submit_btn = st.button("画像を解析")
    image_data = camera_image

# 解析実行
if submit_btn:
    with st.spinner("解析中..."):
        model = model = genai.GenerativeModel('gemini-1.5-flash') # 最新モデルを使用

        if image_data:
            # 画像がアップロードされている場合
            img = Image.open(image_data)
            response = model.generate_content(["この画像に写っている英文を読み取り、構文解析して解説してください。", img])
            st.image(img, caption="撮影された画像", use_column_width=True)
            st.write(response.text)

        elif input_method == "テキスト入力" and user_text:
            # テキストの場合
            response = model.generate_content(f"この英文を構文解析して解説してください: {user_text}")
            st.write(response.text)
        else:
            st.warning("入力（テキストまたは撮影）が必要です")
