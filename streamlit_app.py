import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_triangle(angle_deg, side_length):
    # 角度をラジアンに変換
    angle_rad = np.deg2rad(angle_deg)

    # 三角形の頂点を計算する
    # 原点(0, 0)を固定点として、1辺の長さを指定
    A = np.array([0, 0])
    B = np.array([side_length, 0])
    C = np.array([side_length * np.cos(angle_rad), side_length * np.sin(angle_rad)])

    # 頂点を配列にまとめる
    triangle = np.array([A, B, C, A])

    # プロットの設定
    fig, ax = plt.subplots()
    ax.plot(triangle[:, 0], triangle[:, 1], 'b-')  # 青い線で描画
    ax.fill(triangle[:, 0], triangle[:, 1], 'lightblue')  # 軽い青で塗りつぶし

    # 軸の設定
    ax.set_xlim(-0.1, side_length + 0.1)
    ax.set_ylim(-0.1, side_length + 0.1)
    ax.set_aspect('equal')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title(f'Triangle with Angle {angle_deg}° and Side Length {side_length}')

    return fig

def main():
    st.title('Triangle Drawing with Angle and Side Length')

    # サイドの長さと角度を入力
    side_length = st.slider('Side Length', min_value=1.0, max_value=10.0, value=5.0)
    angle_deg = st.slider('Angle (degrees)', min_value=30, max_value=150, value=60)

    # 三角形をプロット
    fig = plot_triangle(angle_deg, side_length)

    # Matplotlibの図をStreamlitで表示
    st.pyplot(fig)

if __name__ == "__main__":
    main()
