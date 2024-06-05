import streamlit as st
import pandas as pd
import numpy as np

# 世界遺産の位置情報
world_heritage_data = pd.DataFrame({
    '名前': ['キリマンジャロ', 'エーゲ海の島々', 'クスコ歴史地区'],
    '緯度': [-3.0674, 37.3635, -13.5183],
    '経度': [37.3556, 25.2757, -71.9789]
})

st.title("世界歴史検索")

# 世界遺産の位置情報を含むデータフレームを作成
df = pd.DataFrame({
    'lat': world_heritage_data['緯度'],
    'lon': world_heritage_data['経度']
})

# 地図上に世界遺産のピンを表示
st.map(df)
