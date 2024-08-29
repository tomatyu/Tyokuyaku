import streamlit as st
from janome.tokenizer import Tokenizer
import pandas as pd

# 関数: データの読み込み
def load_data():
    try:
        return pd.read_excel("56.xlsx")  # Excelファイルのパスと拡張子を確認してください
    except Exception as e:
        st.error(f"ファイルの読み込みに失敗しました: {e}")
        return pd.DataFrame()  # 空のデータフレームを返す

# 初期設定
st.title('古文自動直訳ツール')

# 入力ボックス
text_input = st.text_area('古文テキストを入力してください', height=200)

# データの読み込み
countries_df = load_data()

# 文節分割処理
if text_input:
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text_input)
    
    # 文節ごとに分割
    segments = [token.surface for token in tokens]

    # ボタンがクリックされたときの処理
    if st.button('直訳を表示'):
        meanings = []
        for segment in segments:
            kv = countries_df[countries_df["古文"] == segment]
            if not kv.empty:
                meanings.append(kv["意味"].iloc[0])
            else:
                meanings.append(f"{segment} ")
        
        st.subheader('文節ごとの直訳結果')
        st.write(" / ".join(meanings))
