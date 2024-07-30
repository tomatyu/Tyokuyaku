import streamlit as st
import pandas as pd

# Excelをロードする関数
def load_data():
    try:
        return pd.read_excel("2s.xlsx")  # Excelファイルのパスと拡張子を確認してください
    except Exception as e:
        st.error(f"ファイルの読み込みに失敗しました: {e}")
        return pd.DataFrame()  # 空のデータフレームを返す

# データの読み込み
countries_df = load_data()

# サイドバーでの単語入力
st.sidebar.header("単語入力")
inputs = [st.sidebar.text_input(f"単語 {i+1}", key=f"input_{i}") for i in range(60)]

# メインエリア
st.title("$古文直訳writer$")
st.write("上から文節ごとに:red[ひらがなで]入力してください。（最大60単語適応）")

# 「直訳を表示」ボタンがクリックされたときの処理
if st.button('直訳を表示'):
    meanings = []
    for word in inputs:
        if word.strip() != "":  # 空でない単語のみ検索
            kv = countries_df[countries_df["古文"] == word]
            if not kv.empty:
                meanings.append(kv["意味"].iloc[0])
            else:
                meanings.append(f"'{word}' の検索結果が見つかりませんでした")
        else:
            meanings.append("")
    
    # 検索結果を表示
    st.write(" ".join(meanings))
