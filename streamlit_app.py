import streamlit as st

# カウントを保存するためのファイル名
COUNTER_FILE_1 = 'counter1.txt'
COUNTER_FILE_2 = 'counter2.txt'

# カウントをファイルから読み込む関数
def load_count(file_name):
    try:
        with open(file_name, 'r') as file:
            count = int(file.read())
    except FileNotFoundError:
        count = 0
    except ValueError:
        count = 0
    return count

# カウントをファイルに保存する関数
def save_count(file_name, count):
    with open(file_name, 'w') as file:
        file.write(str(count))

# カウントをリセットする関数
def reset_count(file_name):
    save_count(file_name, 0)

# Streamlitアプリケーション
def main():
    st.title('2つのカウントアプリ')

    # カウントの読み込み
    count1 = load_count(COUNTER_FILE_1)
    count2 = load_count(COUNTER_FILE_2)

    # レイアウトの設定
    col1, col2 = st.columns(2)

    # 1つ目のカウントボタンとリセットボタン
    with col1:
        st.write(f'カウント 1: {count1}')
        if st.button('カウントアップ 1'):
            count1 += 1
            save_count(COUNTER_FILE_1, count1)
            st.write(f'カウント 1: {count1}')
        if st.button('リセット 1'):
            reset_count(COUNTER_FILE_1)
            count1 = 0
            st.write(f'カウント 1: {count1}')

    # 2つ目のカウントボタンとリセットボタン
    with col2:
        st.write(f'カウント 2: {count2}')
        if st.button('カウントアップ 2'):
            count2 += 1
            save_count(COUNTER_FILE_2, count2)
            st.write(f'カウント 2: {count2}')
        if st.button('リセット 2'):
            reset_count(COUNTER_FILE_2)
            count2 = 0
            st.write(f'カウント 2: {count2}')

if __name__ == "__main__":
    main()
