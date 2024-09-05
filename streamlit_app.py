import streamlit as st

# アプリケーションのタイトル
st.title('英文の単語イニシャル抽出アプリ')

# ユーザーからの入力を受け取る
user_input = st.text_area("英文を入力してください:")

# 英文を単語ごとに分け、イニシャルを抽出する
if user_input:
    words = user_input.split()
    initials = [word[0].lower() for word in words if word]  # 各単語のイニシャルを小文字で取得
    st.write('入力された英文の単語イニシャル:')
    st.write(' '.join(initials))
