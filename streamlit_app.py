import streamlit as st
import plotly.graph_objects as go
import numpy as np
from PIL import Image

# Streamlitのタイトル
st.title('球体に世界地図を貼り付け')

# 球体のデータ生成
def generate_sphere(radius=1, resolution=100):
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z

# 球体のサイズ
radius = 2
x, y, z = generate_sphere(radius)

# 地図画像を読み込む
map_image = Image.open('world_map.jpg')
map_image = map_image.resize((x.shape[1], x.shape[0]))  # 画像サイズを調整
map_image = np.array(map_image) / 255.0  # 画像を0-1の範囲に正規化

# Plotlyの球体を作成
fig = go.Figure(data=[go.Surface(
    x=x, 
    y=y, 
    z=z, 
    surfacecolor=map_image[:, :, 0],  # 画像の赤チャンネルを使用（グレースケールに変換）
    colorscale='Viridis', 
    cmin=0, 
    cmax=1,
    showscale=False
)])

fig.update_layout(
    scene=dict(
        xaxis=dict(nticks=4, range=[-radius-0.5, radius+0.5]),
        yaxis=dict(nticks=4, range=[-radius-0.5, radius+0.5]),
        zaxis=dict(nticks=4, range=[-radius-0.5, radius+0.5]),
        aspectratio=dict(x=1, y=1, z=1)
    ),
    title='球体に世界地図を貼り付けた表示'
)

# Streamlitで球体を表示
st.plotly_chart(fig)
