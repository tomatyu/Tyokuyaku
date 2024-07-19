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

    # ソート後のデータを表示
    st.subheader('数値列を小さい順にソートした結果')
    st.dataframe(sorted_df)
    select =  sorted_df.iloc[0]

if __name__ == '__main__':
    main()
