import streamlit as st
import pandas as pd

# Excelをロードする関数
def load_data():
    try:
        return pd.read_excel("1s.xlsx")  # Excelファイルのパスと拡張子を確認してください
    except Exception as e:
        st.error(f"ファイルの読み込みに失敗しました: {e}")
        return pd.DataFrame()  # 空のデータフレームを返す

# データの読み込み
countries_df = load_data()

# タイトル
st.title("$古文直訳writer$")
st.write("上から文節ごとに入力していってください。（最大10単語適応）")

# タブの作成
tab1, tab2 = st.tabs(["単語入力", "検索結果"])

# タブ1: 単語入力
with tab1:
    # 単語入力欄
    inputs = [st.text_input(f"単語 {i+1}", key=f"input_{i}") for i in range(10)]
    st.write("入力された単語:")
    for i, word in enumerate(inputs):
        if word.strip():  # 空でない単語のみ表示
            st.write(f"単語 {i+1}: {word}")

# タブ2: 検索結果
with tab2:
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
        st.write("### 検索結果:")
        st.write(" ".join(meanings))
