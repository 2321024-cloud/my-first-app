import streamlit as st
import random

st.title("💖 기분 좋아지는 칭찬 앱")
words = ["오늘 하루도 정말 멋지게 해냈어요!", "당신은 생각보다 훨씬 강한 사람입니다.", "실수 좀 하면 어때요? 다 과정인걸요!"]

if st.button("나에게 칭찬 한마디!"):
    st.write(random.choice(words))
