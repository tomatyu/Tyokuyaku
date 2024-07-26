import streamlit as st
import pandas as pd

#　excelをロード
def load_data():
 return pd.read_excel("1s.Axlsx")



countries_df = load_data()
#　タイトル
st.title("_古文直訳writter_")
st.write("上から文節ごとに入力していってください。（最大10単語適応）")
#  単語入力欄
a = st.text_input("")
b = st.text_input("")
c = st.text_input("")
d = st.text_input("")
e = st.text_input("")
f = st.text_input("")
g = st.text_input("")
h = st.text_input("")
i = st.text_input("")
j = st.text_input("")


    
if st.button('国を表示'):
    kv = countries_df[countries_df["国名"] == a]
    kv2 = countries_df[countries_df["国名"] == a]
    kv3 = countries_df[countries_df["国名"] == a]
    kv4 = countries_df[countries_df["国名"] == a]
    kv5 = countries_df[countries_df["国名"] == a]
    kv6 = countries_df[countries_df["国名"] == a]
    kv7 = countries_df[countries_df["国名"] == a]
    kv8 = countries_df[countries_df["国名"] == a]
    kv9 = countries_df[countries_df["国名"] == a]
    kv10 = countries_df[countries_df["国名"] == a]
    if not kv.empty:
        kv_a = kv.iloc[0]
        kv_a = kv["意味"]
        if not kv2.empty:
             kv_b = kv.iloc[0]
             kv_b = kv["意味"]
             if not kv3.empty:
                kv_c = kv.iloc[0]
                kv_c = kv["意味"]
                if not kv4.empty:
                   kv_d = kv.iloc[0]
                   kv_d = kv["意味"]
                   if not kv5.empty:
                      kv_e = kv.iloc[0]
                      kv_e = kv["意味"]
                      if not kv6.empty:
                         kv_f = kv.iloc[0]
                         kv_f = kv["意味"]
                         if not kv7.empty:
                            kv_g = kv.iloc[0]
                            kv_g = kv["意味"]
                            if not kv8.empty:
                               kv_h = kv.iloc[0]
                               kv_h = kv["意味"]
                               if not kv9.empty:
                                  kv_i = kv.iloc[0]
                                  kv_i = kv["意味"]
                                  if not kv10.empty:
                                      kv_j = kv.iloc[0]
                                      kv_j = kv["意味"]
                                      st.write(kv_a,kv_b,kv_c,kv_d,kv_e,kv_f,kv_g,kv_h,kv_i,kv_j)
else:
                st.write("検索結果なし")

