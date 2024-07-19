import streamlit as st

# オセロの初期配置のボードを生成する関数
def generate_board():
    board = [[' ' for _ in range(8)] for _ in range(8)]
    board[3][3] = '●'
    board[3][4] = '○'
    board[4][3] = '○'
    board[4][4] = '●'
    return board

# ゲームボードを表示する関数
def print_board(board):
    for i in range(8):
        st.write(' '.join(board[i]))

# 指定した座標に石を置く関数
def place_piece(board, row, col, piece):
    board[row][col] = piece

# ゲームのメインロジック
def main():
    st.title('二人プレイオセロゲーム')
    st.write("プレイヤー1（●）から始めます。")

    # ゲームボードを生成
    board = generate_board()

    # プレイヤーの交代を管理する変数
    current_player = '●'

    # ゲームループ
    while True:
        st.write(f"現在のプレイヤー: {current_player}")

        # ボードを表示
        print_board(board)

        # プレイヤーに手を打たせる
        col = st.number_input(f"{current_player} の手を入力してください（列番号を0から7で指定）:", min_value=0, max_value=7, key=f"{current_player}_col")
        row = st.number_input(f"{current_player} の手を入力してください（行番号を0から7で指定）:", min_value=0, max_value=7, key=f"{current_player}_row")

        # 石を置く
        if board[row][col] == ' ':
            place_piece(board, row, col, current_player)
        else:
            st.warning("そのマスにはすでに石が置かれています。別の場所を選んでください。")
            continue

        # 次のプレイヤーに交代
        if current_player == '●':
            current_player = '○'
        else:
            current_player = '●'

        # ゲーム終了の判定（盤面が埋まった場合）
        if all(all(cell != ' ' for cell in row) for row in board):
            st.write("ゲーム終了！")
            break

        # ボードを更新するためにウィジェットを再描画
        st.text('')

if __name__ == '__main__':
    main()
