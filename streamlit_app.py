import streamlit as st
import pandas as pd

st.title('Excelデータのソート')

# Excelファイルをアップロードするためのウィジェット
def load_data():
    return pd.read_excel("28.xlsx")

if load_data is not None:
    # pandasでExcelファイルを読み込む
    df = pd.read_excel(load_data)
    
    # データを表示
    st.subheader('元のデータ')
    st.dataframe(df)
    
    # 数値列で昇順にソートする
    sorted_df = df.sort_values(by='緯度', ascending=True)
    
    # ソート後のデータを表示
    st.subheader('数値列を小さい順にソートした結果')
    st.dataframe(sorted_df)