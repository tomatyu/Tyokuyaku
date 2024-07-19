import streamlit as st

def main():
    st.title('2x2 Input Bars Example')

    # 2x2の入力バーを作成する
    # それぞれの要素に対してsliderウィジェットを使用する例
    st.subheader('Matrix Input')

    # 行列の要素を格納する2x2のリスト
    matrix = [[0, 0], [0, 0]]

    # 各要素に対して入力バー（slider）を作成する
    for i in range(2):
        for j in range(2):
            matrix[i][j] = st.slider(f'Element [{i}][{j}]', min_value=0, max_value=100, value=0)

    st.subheader('Entered Matrix')
    st.write(matrix)

if __name__ == '__main__':
    main()
