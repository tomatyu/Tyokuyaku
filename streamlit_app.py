import streamlit as st
import pandas as pd
import random

# グローバル変数としてデータフレームを宣言
df = None

# データをランダムに4行抽出して読み込む関数
def load_data():
    global df
    df = pd.read_excel("28.xlsx")
    random_indices = random.sample(range(len(df)), min(4, len(df)))  # ランダムな行インデックスを取得する
    return df.iloc[random_indices]  # ランダムに抽出した行を取得する

def main():
    global df

    st.title('Excelデータのランダムなソート')

    # データがまだ読み込まれていない場合は読み込む
    if df is None:
        df = load_data()

    # 元のデータを表示
    st.subheader('ランダムに選んだデータ（最大4行）')
    st.dataframe(df)

    # 数値列で昇順にソートする
    sorted_df = df.sort_values(by='緯度', ascending=True)

    # ソート後のデータを表示
    st.subheader('数値列を小さい順にソートした結果')
    st.dataframe(sorted_df)

    # データから4つのユニークな国名を取得する
    unique_countries = sorted_df['国名'].unique()
    # ボタン用のラベルをランダムに選ぶ
    button_labels = random.sample(list(unique_countries), 4)

    # ボタンを2x2のグリッドに配置する
    col1, col2 = st.columns(2)
    with col1:
        if st.button(button_labels[0]):
            st.write(f'クリックされたボタン: {button_labels[0]}')
    with col2:
        if st.button(button_labels[1]):
            st.write(f'クリックされたボタン: {button_labels[1]}')

    with col1:
        if st.button(button_labels[2]):
            st.write(f'クリックされたボタン: {button_labels[2]}')
    with col2:
        if st.button(button_labels[3]):
            st.write(f'クリックされたボタン: {button_labels[3]}')

if __name__ == '__main__':
    main()
if st.button:
    st.write("今日は")
