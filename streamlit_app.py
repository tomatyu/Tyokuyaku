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

    if st.button("ランダム"):
        # ランダムに4つの国名を選ぶ
        sorted_df = df.sort_values(by='緯度', ascending=True)
        unique_countries = sorted_df['国名'].unique()
        if len(unique_countries) >= 4:
            button_labels = random.sample(list(unique_countries), 4)
        else:
            button_labels = list(unique_countries)

    # ボタンの状態を保持するための辞書を初期化
    button_clicked = {label: False for label in button_labels}

    # 選択された国名を保持するリスト
    selected_countries = []

    # ボタンが押されたかどうかを判定し、状態を更新する
    col1, col2 = st.columns(2)
    with col1:
        if button_labels and st.button(button_labels[0]) and not button_clicked[button_labels[0]]:
            button_clicked[button_labels[0]] = True
            selected_countries.append(button_labels[0])
    with col2:
        if len(button_labels) > 1 and st.button(button_labels[1]) and not button_clicked[button_labels[1]]:
            button_clicked[button_labels[1]] = True
            selected_countries.append(button_labels[1])

    with col1:
        if len(button_labels) > 2 and st.button(button_labels[2]) and not button_clicked[button_labels[2]]:
            button_clicked[button_labels[2]] = True
            selected_countries.append(button_labels[2])
    with col2:
        if len(button_labels) > 3 and st.button(button_labels[3]) and not button_clicked[button_labels[3]]:
            button_clicked[button_labels[3]] = True
            selected_countries.append(button_labels[3])

    # 選択された国名を表示する
    if selected_countries:
        st.subheader('選択された国名')
        st.write(selected_countries)


if __name__ == '__main__':
    main()
