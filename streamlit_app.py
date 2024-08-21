import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_triangle():
    fig, ax = plt.subplots()

    # 三角形の頂点を定義
    triangle = np.array([[0, 0], [1, 0], [0.5, 1], [0, 0]])

    # 三角形をプロット
    ax.plot(triangle[:, 0], triangle[:, 1], 'b-')  # 青い線で描画
    ax.fill(triangle[:, 0], triangle[:, 1], 'lightblue')  # 軽い青で塗りつぶし

    # 軸の設定
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
    ax.set_aspect('equal')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Triangle')

    return fig

def main():
    st.title('Triangle Drawing with Streamlit and Matplotlib')
    
    # 三角形をプロット
    fig = plot_triangle()
    
    # Matplotlibの図をStreamlitで表示
    st.pyplot(fig)

if __name__ == "__main__":
    main()
