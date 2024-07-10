import streamlit as st
import pandas as pd

def create_empty_board(size):
    # 空のデータフレームを作成する
    board = pd.DataFrame('', index=range(size), columns=range(size))
    return board

def main():
    st.title('空白の9x9の盤面')

    # 9x9の盤面を作成する
    board_size = 9
    board = create_empty_board(board_size)

    # 盤面を表示する
    selected_position = st.empty()  # ユーザーが選択した位置を表示するための空のコンポーネント

    # 盤面を描画する
    for i in range(board_size):
        row = []  # 各行のボタンを保持するリスト
        for j in range(board_size):
            cell = st.button(f'[{i},{j}]')  # 各マス目をボタンとして表示
            row.append(cell)
        
        # 各行のボタンを横に並べて表示
        st.write(row)
        
        # ユーザーがボタンをクリックしたら位置を表示する
        for j in range(board_size):
            if row[j].clicked:
                selected_position.write(f'選択されたマス: [{i},{j}]')  # ボタンがクリックされたら位置を表示

if __name__ == '__main__':
    main()
