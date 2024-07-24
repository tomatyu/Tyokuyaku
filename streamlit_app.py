import streamlit as st
import pandas as pd
import random

# グローバル変数としてデータフレームを宣言
df = None
selected_country = None  # 選択された国名を保持する変数

# 初期データの読み込み
def load_data():
    global df, selected_country
    df = pd.read_excel("28.xlsx")
    selected_country = df.loc[df['緯度'].idxmin(), '国名']  # 緯度が最小の国を初期選択国とする

def main():
    global df, selected_country

    # データがまだ読み込まれていない場合は初回読み込み
    if df is None:
        load_data()

    st.title('国名クイズ')

    # 問題更新のボタン
    if st.button("問題を更新"):
        update_question()

    # 固定の選択肢として selected_country を含むランダムな3つの国を選ぶ
    unique_countries = df['国名'].unique()
    other_countries = random.sample(list(unique_countries), 3)
    options = [selected_country] + other_countries
    random.shuffle(options)

    # 選択肢を表示
    st.subheader('以下の国の中から、どれが緯度が最小の国でしょう？')
    col1, col2 = st.columns(2)
    with col1:
        if st.button(options[0]):
            check_answer(options[0])
    with col2:
        if st.button(options[1]):
            check_answer(options[1])
    with col1:
        if st.button(options[2]):
            check_answer(options[2])
    with col2:
        if st.button(options[3]):
            check_answer(options[3])

def update_question():
    global selected_country

    # データからランダムに新しい問題を選ぶ
    unique_countries = df['国名'].unique()
    selected_country = random.choice(unique_countries)

    # 問題を更新したことを通知
    st.write("新しい問題を更新しました！")

def check_answer(answer):
    global selected_country

    # 選択された国が正解かどうかを判定
    if answer == selected_country:
        st.write("正解！")
    else:
        st.write("不正解…")

if __name__ == '__main__':
    main()
