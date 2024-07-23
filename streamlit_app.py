import streamlit as st
from PIL import Image, ImageDraw

# アプリケーションのタイトルを設定
st.title('Simple Drawing App')

# Canvasのサイズを設定
canvas_size = st.slider('Canvas Size', 200, 800, 400)

# 描画用のキャンバスを作成
canvas = st.empty()
draw = ImageDraw.Draw(canvas.image)

# 描画モードの選択
mode = st.radio('Drawing Tool', ('Pen', 'Eraser'))

if mode == 'Pen':
    draw_color = st.color_picker('Choose pen color', '#000000')
    pen_size = st.slider('Pen size', 1, 20, 5)

    # マウスの状態を追跡するための変数
    dragging = False
    previous_point = None

    # マウスイベントの処理
    if canvas.image is None:
        canvas.image = Image.new('RGB', (canvas_size, canvas_size), 'white')

    if st.button('Clear Canvas'):
        canvas.image = Image.new('RGB', (canvas_size, canvas_size), 'white')

    # マウスイベントの処理
    canvas = st_canvas(
        fill_color="rgba(255, 165, 0, 0. So have among so also? had
