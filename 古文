import streamlit as st
import pandas as pd

# セッション状態に「input」が存在しない場合、初期化
if 'input' not in st.session_state:
    st.session_state.input = ""

# 入力フィールドの表示とセッション状態への保存
user_input = st.text_input("Enter something:", value=st.session_state.input)
st.session_state.input = user_input

# ページの上部にユーザーの入力内容を表示
st.write(f"Your input: {st.session_state.input}")

# Excelをロードする関数
def load_data():
    try:
        return pd.read_excel("1s.xlsx")  # Excelファイルの拡張子を確認してください
    except Exception as e:
        st.error(f"ファイルの読み込みに失敗しました: {e}")
        return pd.DataFrame()  # 空のデータフレームを返す

# データの読み込み
countries_df = load_data()

# タイトル
st.title("$古文直訳writer$")
st.write("上から文節ごとに入力していってください。（最大10単語適応）")

# 単語入力欄
inputs = [st.text_input(f"単語 {i+1}") for i in range(10)]

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
    
    # 検索結果の表示
    st.write("検索結果:")
    st.write(" ".join(meanings))
