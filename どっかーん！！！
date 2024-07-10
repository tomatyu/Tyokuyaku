import streamlit as st
import pandas as pd

# フランスの緯度と経度
france_latitude = 46.603354
france_longitude = 1.888334

# DataFrameを作成
france_df = pd.DataFrame({
    'lat': [france_latitude],
    'lon': [france_longitude]
})

# 地図にピンを立てる
st.map(france_df)
