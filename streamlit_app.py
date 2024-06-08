import streamlit as st

# フランスの緯度と経度
france_latitude = 46.603354
france_longitude = 1.888334

# ピンを立てる
st.map([[france_latitude, france_longitude]])
