import streamlit as st
import pandas as pd
import numpy as np

# ヨーロッパのデータを生成
europe_lat = np.random.uniform(35, 70, 100)
europe_lon = np.random.uniform(-10, 40, 100)
df = pd.DataFrame({'lat': europe_lat, 'lon': europe_lon})

st.title("ヨーロッパの地図")

# ヨーロッパの中心座標
europe_center = [51.1657, 10.4515]

# Folium地図の作成
st.map(df, center=europe_center, zoom=4)
