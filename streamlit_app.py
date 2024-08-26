import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Streamlitのタイトル
st.title('球体に模擬地図を貼り付け')

# 球体のデータ生成
def generate_sphere(radius=1, resolution=100):
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z

# 簡単な模擬地図データの生成
def generate_map_texture(resolution=100):
    # 模擬地図としてランダムなノイズを生成
    texture = np.random.rand(resolution, resolution, 3)
    return texture

# 球体のサイズ
radius = 100
x, y, z = generate_sphere(radius)

# 模擬地図データを生成
map_texture = generate_map_texture(x.shape[0])

# Plotlyの球体を作成
fig = go.Figure(data=[go.Surface(
    x=x,
    y=y,
    z=z,
    surfacecolor=map_texture[:, :, 0],  # 赤チャンネルを使用
    colorscale='Viridis',
    cmin=0,
    cmax=1,
    showscale=False
)])

fig.update_layout(
    scene=dict(
        xaxis=dict(nticks=100, range=[-radius-0.5, radius+0.5]),
        yaxis=dict(nticks=100, range=[-radius-0.5, radius+0.5]),
        zaxis=dict(nticks=100, range=[-radius-0.5, radius+0.5]),
        aspectratio=dict(x=1, y=1, z=1)
    ),
    title='球体に模擬地図を貼り付けた表示'
)

# Streamlitで球体を表示
st.plotly_chart(fig)
