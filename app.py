import streamlit as st
import random

st.title("🗣️ 조음 연습 단어 뽑기 앱")
st.write("오늘 연습할 발음을 선택하고 단어를 뽑아보세요!")

# 연습할 소리 선택하기
target_sound = st.radio(
    "어떤 소리를 연습할까요?",
    ["'ㅅ' 소리", "'ㄹ' 소리", "'ㅊ' 소리"]
)

# 소리별 타겟 단어 리스트
s_words = ["사과", "사자", "수박", "소방차", "시계", "사진", "사슴"]
r_words = ["라면", "오리", "기린", "로봇", "비행기", "모래", "호랑이"]
ch_words = ["치즈", "기차", "참새", "초콜릿", "고추", "치약", "타조"]

# 버튼을 누르면 실행되는 부분
if st.button("연습 단어 뽑기! 🎯"):
    # 선택한 소리에 맞춰서 단어 리스트 설정
    if target_sound == "'ㅅ' 소리":
        choice = random.choice(s_words)
    elif target_sound == "'ㄹ' 소리":
        choice = random.choice(r_words)
    elif target_sound == "'ㅊ' 소리":
        choice = random.choice(ch_words)
        
    # 결과 출력
    st.subheader(f"크게 따라해 보세요: **{choice}**")
    
    # 칭찬 풍선 효과
    st.balloons()
