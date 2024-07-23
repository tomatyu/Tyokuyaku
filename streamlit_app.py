import streamlit as st
from PIL import Image, ImageDraw

# アプリケーションのタイトルを設定
st.title('Simple Drawing App')

# Canvasのサイズを設定
canvas_size = st.slider('Canvas Size', 200, 800, 400)

# 描画用のキャンバスを作成
canvas_image = Image.new('RGB', (canvas_size, canvas_size), 'white')
draw = ImageDraw.Draw(canvas_image)

# 描画モードの選択
mode = st.radio('Drawing Tool', ('Pen', 'Eraser'))

if mode == 'Pen':
    draw_color = st.color_picker('Choose pen color', '#000000')
    pen_size = st.slider('Pen size', 1, 20, 5)

    # マウスの状態を追跡するための変数
    dragging = False
    previous_point = None

    # マウスイベントの処理
    def draw_on_image(image, draw, start, end, color, size):
        draw.line([start, end], fill=color, width=size)
        return image

    if st.button('Clear Canvas'):
        canvas_image = Image.new('RGB', (canvas_size, canvas_size), 'white')

    # 描画ツールのロジックを追加する

# Streamlitの画面にキャンバスを表示する
st.image(canvas_image)

# 必要な場所で最終のcanvas_imag
