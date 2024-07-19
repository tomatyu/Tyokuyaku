import streamlit as st
import pandas as pd
import random

# データをランダムに4つ抽出して読み込む関数
def load_data():
    df = pd.read_excel("28.xlsx")
    num_rows = min(4, len(df))  # 最大4つのデータを抽出する
    indices = random.sample(range(len(df)), num_rows)  # ランダムな行インデックスを取得する
    datasets = [df.iloc[idx] for idx in indices]  # ランダムに抽出したデータセットを取得する
    return datasets

def main():
    st.title('ランダムなExcelデータセットのソート')

    # データを読み込む
    datasets = load_data()

    # 各データセットを表示し、数値列で昇順にソートする
    for i, df in enumerate(datasets):
        st.subheader(f'ランダムなデータセット{i+1}（最初の4行）')
        st.dataframe(df)

        # 数値列で昇順にソートする
        sorted_df = df.sort_values(by='列名', ascending=True)

        # ソート後のデータを表示
        st.subheader(f'データセット{i+1}を小さい順にソートした結果')
        st.dataframe(sorted_df)

if __name__ == '__main__':
    main()
