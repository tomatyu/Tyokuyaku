import streamlit as st
import pandas as pd

# サイドバーに国名と首都を表示
st.sidebar.write("国名: アメリカ合衆国")
st.sidebar.write("首都: ワシントンDC")

# データフレームの作成
usa_df = pd.DataFrame({
    'lat': [38.8977],  # ワシントンDCの緯度
    'lon': [-77.0365]  # ワシントンDCの経度
})

# メインエリアに地図を表示
st.map(usa_df, zoom = 1)
