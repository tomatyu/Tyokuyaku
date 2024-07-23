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

    # ボタンのラベルをランダムに設定する
    button_labels = random.sample(list(sorted_df['国名']), 4)

    # ボタンを生成してクリックされた順番を記録する
    clicked_order = []
    col1, col2 = st.columns(2)
    for label in button_labels:
        with col1:
            if st.button(label):
                clicked_order.append(label)
        with col2:
            if st.button(label):
                clicked_order.append(label)

    # 正しい順番を取得する
    correct_order = sorted_df['国名'].tolist()

    # 結果を判定する
    if clicked_order == correct_order:
        st.write("正解です")
    else:
        st.write("不正解です")

if __name__ == '__main__':
    main()
