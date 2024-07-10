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
    st.dataframe(board.style.applymap(lambda x: 'background-color: white').set_properties(**{'text-align': 'center'}))

if __name__ == '__main__':
    main()
