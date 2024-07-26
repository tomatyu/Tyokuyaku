import streamlit as st
import pandas as pd

# Excelをロードする関数
def load_data():
    return pd.read_excel("1s.Axlsx")

# データの読み込み
countries_df = load_data()

# タイトル
st.title("_古文直訳writer_")
st.write("上から文節ごとに入力していってください。（最大10単語適応）")

# 単語入力欄
inputs = [st.text_input(f"単語 {i+1}") for i in range(10)]

# 「国を表示」ボタンがクリックされたときの処理
if st.button('国を表示'):
    meanings = []
    for word in inputs:
        if word.strip() != "":  # 空でない単語のみ検索
            kv = countries_df[countries_df["国名"] == word]
            if not kv.empty:
                meanings.append(kv["意味"].iloc[0])
            else:
                meanings.append(f"'{word}' の検索結果が見つかりませんでした")
        else:
            meanings.append("入力が空です")
    
    # 検索結果の表示
    st.write("検索結果:")
    st.write(" ".join(meanings))
