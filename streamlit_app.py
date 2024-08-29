import streamlit as st

# カウントを保存するためのファイル名
COUNTER_FILE = 'counter.txt'

# カウントをファイルから読み込む関数
def load_count():
    try:
        with open(COUNTER_FILE, 'r') as file:
            count = int(file.read())
    except FileNotFoundError:
        count = 0
    except ValueError:
        count = 0
    return count

# カウントをファイルに保存する関数
def save_count(count):
    with open(COUNTER_FILE, 'w') as file:
        file.write(str(count))

# Streamlitアプリケーション
def main():
    st.title('カウントアプリ')
    
    # 現在のカウントを読み込む
    count = load_count()
    
    # カウント表示
    st.write(f'現在のカウント: {count}')
    
    # ボタンが押されたときの処理
    if st.button('カウントアップ'):
        count += 1
        save_count(count)
        

if __name__ == "__main__":
    main()
