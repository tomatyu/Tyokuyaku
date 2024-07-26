import streamlit as st
import pandas as pd
import random

# グローバル変数としてデータフレームを宣言
df = None
selected_country = None  # 選択された国名を保持する変数
min_latitude_country = None  # 最小の緯度を持つ国名を保持する変数
options = []  # 選択肢を保持するリスト

# 初期データの読み込み
def load_data():
    global df, selected_country, min_latitude_country
    df = pd.read_excel("28.xlsx")
    min_latitude_country = df.loc[df['緯度'].idxmin(), '国名']  # 緯度が最小の国を初期選択国とする
    selected_country = min_latitude_country  # 最初の問題として最小緯度の国名を設定

def main():
    global df, selected_country, min_latitude_country, options

    # データがまだ読み込まれていない場合は初回読み込み
    if df is None:
        load_data()

    st.title('国名クイズ')

    # 問題更新のボタン
    if st.button("問題を更新"):
        update_question()
    
    # 選択肢がまだ設定されていない場合は初回設定
    if not options:
        update_question()

    # 問題の表示
    st.subheader('以下の国の中から、どれが緯度が最小の国でしょう？')
    
    # ボタンを使って選択肢を表示
    cols = st.columns(2)
    for i, option in enumerate(options):
        with cols[i % 2]:
            if st.button(option):
                check_answer(option)

def update_question():
    global selected_country, options

    # データから新しい問題を選ぶ
    unique_countries = df['国名'].unique()
    new_selected_country = random.choice(unique_countries)

    # 最小緯度の国名と同じ場合、別の国名を選ぶ
    while new_selected_country == min_latitude_country:
        new_selected_country = random.choice(unique_countries)

    selected_country = new_selected_country

    # 選択肢を設定
    other_countries = random.sample(list(unique_countries), 3)
    options = [selected_country] + other_countries
    random.shuffle(options)

    # 問題を更新したことを通知
    st.session_state.message = "新しい問題を更新しました！"

def check_answer(answer):
    global selected_country

    # 選択された国が正解かどうかを判定
    if answer == selected_country:
        st.session_state.message = "正解！"
    else:
        st.session_state.message = "不正解…"

    # メッセージを表示
    st.write(st.session_state.message)

if __name__ == '__main__':
    main()
