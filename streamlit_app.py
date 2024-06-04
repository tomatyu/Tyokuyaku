import streamlit as st
import plotly.graph_objects as go

# タイトルを表示
st.title('World Map with Streamlit')

# 地図の描画
fig = go.Figure(data=go.Scattergeo(
    lon = [0],
    lat = [0],
    mode = 'markers'
))

fig.update_geos(projection_type="natural earth")
st.plotly_chart(fig)

