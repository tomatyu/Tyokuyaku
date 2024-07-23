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

    # ボタン用のラベルをランダムに選ぶ
    sorted_df = df.sort_values(by='緯度', ascending=True)
    unique_countries = sorted_df['国名'].unique()
    button_labels = random.sample(list(unique_countries), 4)

    # ボタンを2x2のグリッドに配置する
    col1, col2 = st.columns(2)

    # ボタンが押されたかどうかの状態を保持する辞書
    button_clicked = {
        button_labels[0]: False,
        button_labels[1]: False,
        button_labels[2]: False,
        button_labels[3]: False
    }

    # ボタンが押された場合、そのボタンの状態を更新する
    if st.button(button_labels[0]):
        button_clicked[button_labels[0]] = True
    if st.button(button_labels[1]):
        button_clicked[button_labels[1]] = True
    if st.button(button_labels[2]):
        button_clicked[button_labels[2]] = True
    if st.button(button_labels[3]):
        button_clicked[button_labels[3]] = True

    # ボタンの状態に応じてメッセージを表示する
    selected_countries = [label for label, clicked in button_clicked.items() if clicked]
    if selected_countries:
        st.subheader('選択された国名')
        st.write(selected_countries)


if __name__ == '__main__':
    main()
