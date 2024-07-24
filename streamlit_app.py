import streamlit as st
import pandas as pd
import random

# グローバル変数としてデータフレームを宣言
df = None
selected_countries = []  # 選択された国名を保持するリスト

# 初期データの読み込み
def load_data():
    global df
    df = pd.read_excel("28.xlsx")

def main():
    global df, selected_countries

    # データがまだ読み込まれていない場合は初回読み込み
    if df is None:
        load_data()

    st.title('Excelデータのランダムなソート')
    min_latitude_row = df.loc[df['緯度'].idxmin()]
    country = min_latitude_row['国名']

    # ランダムボタンのクリックとユニークな国名の取得
    if st.button("ランダム"):
        sorted_df = df.sort_values(by='緯度', ascending=True)
        unique_countries = sorted_df['国名'].unique()

        # ユニークな国名がない場合のエラーハンドリング
        if len(unique_countries) < 4:
            st.error("データから4つの国をランダムに選ぶには、少なくとも4つの異なる国が必要です。")
            return

        # ボタンのラベルをランダムに選ぶ
        button_labels = random.sample(list(unique_countries), 4)

        # 選択された国名を表示する
        col1, col2 = st.columns(2)

        with col1:
            if st.button(button_labels[0]):
                selected_countries.append(button_labels[0])
        with col2:
            if st.button(button_labels[1]):
                selected_countries.append(button_labels[1])

        with col1:
            if st.button(button_labels[2]):
                selected_countries.append(button_labels[2])
        with col2:
            if st.button(button_labels[3]):
                selected_countries.append(button_labels[3])

    # ユーザーが選んだ国名と正解を比較して結果を表示
    if selected_countries:
        st.subheader('選択された国名')
        st.write(selected_countries)

        # 正解判定
        if country in selected_countries:
            st.write("正解")
        else:
            st.write("不正解")

if __name__ == '__main__':
    main()
