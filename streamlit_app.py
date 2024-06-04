import streamlit as st
import plotly.express as px
pip install plotly
# タイトルを表示
st.title('World Map with Streamlit')

# 地図の描画
fig = px.scatter_geo(lat=[0], lon=[0])
fig.update_geos(projection_type="natural earth")
st.plotly_chart(fig)
