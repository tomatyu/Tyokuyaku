import streamlit as st
import pandas as pd
import random

# データをランダムに4行抽出して読み込む関数
def load_data():
    df = pd.read_excel("28.xlsx")
    random_indices = random.sample(range(len(df)), min(4, len(df)))  # ランダムな行インデックスを取得する
    return df.iloc[random_indices]  # ランダムに抽出した行を取得する

def main():
    st.title('Excelデータのランダムなソート')

    # データを読み込む
    df = load_data()

    # 元のデータを表示
    st.subheader('ランダムに選んだデータ（最大4行）')
    st.dataframe(df)

    # 数値列で昇順にソートする
    sorted_df = df.sort_values(by='緯度', ascending=True)

    # 国名のリストを作成
    countries = sorted_df["国名"].tolist()

    # ボタンを1回ずつしか押せないようにするためのフラグ
    button_pressed = [False] * 4

    col1, col2 = st.columns(2)

    with col1:
        if st.button(countries[0]):
            button_pressed[0] = True

    with col2:
        if st.button(countries[1]):
            button_pressed[1] = True

    with col1:
        if st.button(countries[2]):
            button_pressed[2] = True

    with col2:
        if st.button(countries[3]):
            button_pressed[3] = True

    # 正しい順序でボタンが押されたかを判定
    if all(button_pressed):
        st.write("正解です")
    else:
        st.write("不正解です")

if __name__ == '__main__':
    main()
