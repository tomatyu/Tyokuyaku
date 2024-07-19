import streamlit as st
import random

def main():
    st.title("選択項目の正誤チェック")

    options = ["項目A", "項目B", "項目C", "項目D"]  # リストの選択肢

    selected_option = st.selectbox("項目を選択してください:", options)

    if st.button("選択した項目の正誤をチェック"):
        # ここではランダムに選択した項目が正しいかどうかを決定する
        is_correct = random.choice([True, False])

        if is_correct:
            st.success(f"{selected_option} は正しいです！")
        else:
            st.error(f"{selected_option} は正しくありません。")

if __name__ == "__main__":
    main()
