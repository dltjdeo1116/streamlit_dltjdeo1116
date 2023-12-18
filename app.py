import streamlit as st
from st_pages import Page, show_pages, add_page_title

st.set_page_config(
      page_title="통계 포스터 만들기",
      page_icon="clipboard",
      layout="centered"
)


st.markdown("<h1 style='text-align: center;'>통계 포스터 만들기</h1>", unsafe_allow_html=True)
st.divider()

st.subheader(':pencil2: 통계 포스터란?')
st.write("**통계포스터는 :blue[하나 이상의 연관된 그래프] 를 사용해 자료를 요약하고, 여러 관점에서 문제에 접근하는 과정에서 문제의 해답을 찾고, 자료를 분석한 것을 시각적으로 보여주는 자료입니다.**")
st.write("**기존 탐구보고서와 비슷하지만 :blue[문제해결과정에서 통계가 반드시 사용되어야한다는 점]과 여러 장이 아닌 :blue[커다란 종이 한장]에 만들어 주제(문제제기), 문제해결방법, 통계분석결과, 논의 사항, 결론 등의 논리적인 흐름을 따라가면서 한눈에 내용을 확인할 수 있도록 시각적으로 표현한다는 점이 다른 점입니다.**")

video_url= "https://www.youtube.com/watch?v=-koa8iAGK3E&t=11s"
st.video(video_url, format='video/mp4')

st.divider()

st.subheader(':pencil2: 통계 포스터 제작 순서')
st.write("")
st.subheader(":gray[주제선정] :gray[➡️] :gray[자료수집 방법 결정] :gray[➡️] :gray[데이터 수집과 분석] ")
st.subheader(":gray[➡️]  :gray[통계포스터 제작]")

st.divider()

st.subheader(':pencil2: 2023년 전국학생통계활용대회 수상작')

tool = [
    {
        "image": r'images/image1.png',
    },
    {
        "image": r'images/image2.png',
    },    
    {
        "image": r'images/image3.png',
    },
    {
        "image": r'images/image4.png',
    },
    {
        "image": r'images/image5.png',
    },
    {
        "image": r'images/image6.png',
    },
    {
        "image": r'images/image7.png',
    },
    {
        "image": r'images/image8.png',
    },
    {
        "image": r'images/image9.png',
    },
]

for i in range(0,len(tool),3):
    row_tool = tool[i:i+3]
    cols = st.columns(3)
    
    for j in range(len(row_tool)):
        with cols[j%3]:
            current_pet = row_tool[j]
            st.image(current_pet["image"])

st.link_button("다양한 수상작 확인하기(통계활용대회)", "https://www.xn--989a71jnrsfnkgufki.kr/report/awardView.do?seq=131")

show_pages(
    [
        Page("app.py", "통계포스터란?"),
        Page("page1.py", "1. 자료선정"),
        Page("page2.py", "2. 자료수집 방법 결정"),
        Page("page3.py", "3. 데이터 수집과 분석"),
        Page("page4.py", "3-1. 예제 실습"),
        Page("page5.py", "3-2. 예제 실습"),
        Page("page6.py", "4. 통계포스터 제작"),
    ]
)