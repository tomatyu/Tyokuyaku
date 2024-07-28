import streamlit as st
import pandas as pd
import random

# グローバル変数としてデータフレームを宣言
df = None
options = []  # 選択肢を保持するリスト

# 初期データの読み込み
def load_data():
    global df
    df = pd.read_excel("28.xlsx")

# 新しい問題を更新する関数
def update_question():
    global options

    # データから選択肢を設定
    unique_countries = df['国名'].unique()
    
    # ランダムに4つの国を選ぶ
    selected_countries = random.sample(list(unique_countries), 4)
    
    # 4つの国の緯度情報を取得し、最も緯度が低い国を正解とする
    selected_df = df[df['国名'].isin(selected_countries)]
    min_latitude_country = selected_df.loc[selected_df['緯度'].idxmin(), '国名']

    # 選択肢をシャッフルして表示
    options = selected_countries
    random.shuffle(options)

    # セッション状態を更新
    st.session_state.min_latitude_country = min_latitude_country
    st.session_state.options = options
    st.session_state.message = "新しい問題を更新しました！"
    st.session_state.correct = None  # リセットする
    st.session_state.answer_submitted = False  # 回答状態のリセット

# ユーザーの回答をチェックする関数
def check_answer(answer):
    if st.session_state.answer_submitted:
        st.session_state.message = "すでに回答済みです。問題を更新してから再度挑戦してください。"
        return

    if answer == st.session_state.min_latitude_country:
        st.session_state.message = f"正解！正解は「{st.session_state.min_latitude_country}」です。"
        st.session_state.points += 10  # 正解で10ポイント追加
        st.session_state.correct = True
    else:
        st.session_state.message = f"不正解…「{answer}」は正しくありません。正解は「{st.session_state.min_latitude_country}」です。"
        st.session_state.points -= 10  # 不正解で10ポイント減算
        st.session_state.correct = False

    st.session_state.answer_submitted = True  # 回答済みフラグを設定

def main():
    global df

    # データがまだ読み込まれていない場合は初回読み込み
    if df is None:
        load_data()

    st.title('国名クイズ')

    # セッション状態にメッセージ、正解フラグ、ポイント、回答状態がない場合は初期化
    if 'message' not in st.session_state:
        st.session_state.message = ''
    if 'correct' not in st.session_state:
        st.session_state.correct = None
    if 'min_latitude_country' not in st.session_state:
        st.session_state.min_latitude_country = None
    if 'options' not in st.session_state:
        st.session_state.options = []
    if 'points' not in st.session_state:
        st.session_state.points = 0  # 初期ポイントは0
    if 'answer_submitted' not in st.session_state:
        st.session_state.answer_submitted = False  # 回答状態の初期化

    # 現在のポイントを表示
    st.sidebar.subheader('現在のポイント')
    st.sidebar.write(st.session_state.points)

    # 問題更新のボタン
    if st.button("問題を更新"):
        update_question()

    # 選択肢がまだ設定されていない場合は初回設定
    if not st.session_state.options:
        update_question()

    # 問題の表示
    st.subheader('以下の国の中から、どれが最も緯度が低い国でしょう？')

    # ボタンを使って選択肢を表示
    cols = st.columns(2)
    for i, option in enumerate(st.session_state.options):
        with cols[i % 2]:
            # 回答済みかどうかでボタンを無効化する
            if st.session_state.answer_submitted:
                st.button(option, disabled=True, key=f"disabled_{option}")
            else:
                if st.button(option, key=f"option_{option}"):
                    check_answer(option)

    # メッセージを表示
    if st.session_state.message:
        st.write(st.session_state.message)

if __name__ == '__main__':
    main()
