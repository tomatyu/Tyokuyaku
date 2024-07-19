import streamlit as st

# オセロの初期配置のボードを生成する関数
def generate_board():
    board = [[' ' for _ in range(8)] for _ in range(8)]
    board[3][3] = '●'
    board[3][4] = '○'
    board[4][3] = '○'
    board[4][4] = '●'
    return board

# Streamlitアプリケーションのメイン部分
def main():
    st.title('オセロゲーム')

    # ゲームボードを生成
    board = generate_board()

    # ボードを表示
    for i in range(8):
        st.write(' '.join(board[i]))

if __name__ == '__main__':
    main()
