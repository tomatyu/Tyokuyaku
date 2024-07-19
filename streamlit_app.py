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

    # ランダムな順番でボタンを表示するためのインデックスをシャッフル
    random_indices = list(range(4))
    random.shuffle(random_indices)

    col1, col2 = st.columns(2)

    with col1:
        if st.button(countries[random_indices[0]]):
            check_order(countries, random_indices)

    with col2:
        if st.button(countries[random_indices[1]]):
            check_order(countries, random_indices)

    with col1:
        if st.button(countries[random_indices[2]]):
            check_order(countries, random_indices)

    with col2:
        if st.button(countries[random_indices[3]]):
            check_order(countries, random_indices)

def check_order(countries, random_indices):
    # 押された順序を確認する
    correct_order = sorted(countries)
    selected_order = [countries[idx] for idx in random_indices]

    if selected_order == correct_order:
        st.write("正解です")
    else:
        st.write("不正解です")

if __name__ == '__main__':
    main()
