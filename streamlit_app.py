import streamlit as st

# セッション状態に「input」が存在しない場合、初期化
if 'input' not in st.session_state:
    st.session_state.input = ""

# 入力フィールド
user_input = st.text_input("Enter something:", value=st.session_state.input)

# 入力内容をセッション状態に保存
st.session_state.input = user_input

# ページの上部にユーザーの入力内容を表示
st.write(f"Your input: {st.session_state.input}")
