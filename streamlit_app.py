import streamlit as st
import numpy as np

# オセロの初期盤面を作成する関数
def initial_board():
    board = np.zeros((8, 8), dtype=int)
    board[3, 3] = board[4, 4] = 1  # 白石
    board[3, 4] = board[4, 3] = -1  # 黒石
    return board

# 指定された手番の合法手を探索する関数
def legal_moves(board, player):
    moves = []
    for i in range(8):
        for j in range(8):
            if board[i, j] == 0:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), 
                               (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    x, y = i + di, j + dj
                    if 0 <= x < 8 and 0 <= y < 8 and board[x, y] == -player:
                        while 0 <= x < 8 and 0 <= y < 8 and board[x, y] == -player:
                            x, y = x + di, y + dj
                        if 0 <= x < 8 and 0 <= y < 8 and board[x, y] == player:
                            moves.append((i, j))
                            break
    return moves

# 盤面の石の数をカウントする関数
def count_pieces(board):
    black_count = np.sum(board == -1)
    white_count = np.sum(board == 1)
    return black_count, white_count

# 石をひっくり返す関数
def flip(board, player, move):
    i, j = move
    board[i, j] = player
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1),
                   (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        x, y = i + di, j + dj
        if 0 <= x < 8 and 0 <= y < 8 and board[x, y] == -player:
            while 0 <= x < 8 and 0 <= y < 8 and board[x, y] == -player:
                x, y = x + di, y + dj
            if 0 <= x < 8 and 0 <= y < 8 and board[x, y] == player:
                nx, ny = i + di, j + dj
                while (nx, ny) != (x, y):
                    board[nx, ny] = player
                    nx, ny = nx + di, ny + dj
    return board

# ゲームのメインロジック
def play_game():
    board = initial_board()
    st.write("初期盤面:")
    st.write(board)

    st.write("ゲームを開始します。")

    player = 1  # 最初は白番
    while True:
        moves = legal_moves(board, player)
        if len(moves) == 0:
            st.write("パスします。")
            player = -player
            moves = legal_moves(board, player)
            if len(moves) == 0:
                st.write("ゲーム終了です。")
                break

        st.write(f"現在の盤面:")
        for i in range(8):
            for j in range(8):
                if board[i, j] == -1:
                    st.write("◼️", end=" ")
                elif board[i, j] == 1:
                    st.write("◻️", end=" ")
                else:
                    st.write("⬜️", end=" ")
            st.write("")  # 改行

        st.write(f"プレイヤー {player} の番です。")

        # UI上での操作
        move = st.selectbox("どこに置きますか？", moves)
        board = flip(board, player, move)
        player = -player

    black_count, white_count = count_pieces(board)
    st.write(f"最終盤面:")
    for i in range(8):
        for j in range(8):
            if board[i, j] == -1:
                st.write("◼️", end=" ")
            elif board[i, j] == 1:
                st.write("◻️", end=" ")
            else:
                st.write("⬜️", end=" ")
        st.write("")  # 改行
    st.write(f"黒の石: {black_count}, 白の石: {white_count}")

# Streamlit UI
st.title('Streamlit オセロゲーム')

play_game()
