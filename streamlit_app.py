import streamlit as st
import pandas as pd

# データを読み込む関数
def load_data():
    return pd.read_excel("28.xlsx")

def main():
    st.title('Excelデータのソート')

    # データを読み込む
    df = load_data()

    # 元のデータを表示
    st.subheader('元のデータ')
    st.dataframe(df)

    # 数値列で昇順にソートする
    sorted_df = df.sort_values(by='緯度', ascending=True)

    # ソート後のデータを表示
    st.subheader('数値列を小さい順にソートした結果')
    st.dataframe(sorted_df)

if __name__ == '__main__':
    main()
