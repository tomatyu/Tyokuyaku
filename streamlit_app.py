import streamlit as st
import pandas as pd
import random

# グローバル変数としてデータフレームを宣言
df = None

# 初期データの読み込み
def load_data():
    global df
    df = pd.read_excel("28.xlsx")

def main():
    global df

    st.title('Excelデータのランダムなソート')

    # データがまだ読み込まれていない場合は初回読み込み
    if df is None:
        load_data()

    # 数値列で昇順にソートする
    sorted_df = df.sort_values(by='緯度', ascending=True)

    # ソート後のデータを表示
    st.subheader('数値列を小さい順にソートした結果')
    st.dataframe(sorted_df)

    # データから4つのユニークな国名を取得する
    
    # ボタン用のラベルをランダムに選ぶ
if st.button("ランダム"):
    sorted_df = df.sort_values(by='緯度', ascending=True)

    unique_countries = sorted_df['国名'].unique()
    button_labels = random.sample(list(unique_countries), 4)

    # ボタンを2x2のグリッドに配置する
    col1, col2 = st.columns(2)

    # ボタンの状態を保持するための辞書
    button_state = {
        button_labels[0]: False,
        button_labels[1]: False,
        button_labels[2]: False,
        button_labels[3]: False
    }

    # ボタンが押された場合、そのボタンの状態を反転する
    if st.button(button_labels[0]):
        button_state[button_labels[0]] = not button_state[button_labels[0]]
    if st.button(button_labels[1]):
        button_state[button_labels[1]] = not button_state[button_labels[1]]
    if st.button(button_labels[2]):
        button_state[button_labels[2]] = not button_state[button_labels[2]]
    if st.button(button_labels[3]):
        button_state[button_labels[3]] = not button_state[button_labels[3]]

    # ボタンの状態に応じてメッセージを表示する
    with col1:
        if button_state[button_labels[0]]:
            st.write(f'クリックされたボタン: {button_labels[0]}')
    with col2:
        if button_state[button_labels[1]]:
            st.write(f'クリックされたボタン: {button_labels[1]}')

    with col1:
        if button_state[button_labels[2]]:
            st.write(f'クリックされたボタン: {button_labels[2]}')
    with col2:
        if button_state[button_labels[3]]:
            st.write(f'クリックされたボタン: {button_labels[3]}')


if __name__ == '__main__':
    main()
    random
