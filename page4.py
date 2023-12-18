import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import seaborn as sns

# 데이터 파일 로드
df = pd.read_csv('data/학교급 및 시도별 학생 1인당 월평균 사교육비.csv', encoding='cp949')

# Streamlit 애플리케이션 시작
st.title('학교급 및 시도별 학생 1인당 월평균 사교육비 시각화')

# 데이터셋 선택
selected_region = st.selectbox('지역 선택', df['시도별'].unique())

# 선택된 지역의 데이터 필터링
selected_data = df[df['시도별'] == selected_region]

# 그래프 타입 선택
chart_type = st.selectbox('그래프 종류', ['Bar Chart', 'Area Chart', 'Pie Chart', 'Scatter Plot', 'XY Heat map'])

# 그래프 그리기
if chart_type == 'Bar Chart':
    chart = alt.Chart(selected_data).mark_bar().encode(
        x='항목',
        y='2022'
    ).properties(
        title=f'{selected_region} 지역 2022년 학교급별 1인당 월평균 사교육비'
    )
    st.altair_chart(chart, use_container_width=True)

elif chart_type == 'Area Chart':
    chart = alt.Chart(selected_data).mark_area().encode(
        x='항목',
        y='2022'
    ).properties(
        title=f'{selected_region} 지역 2022년 학교급별 1인당 월평균 사교육비 (Area Chart)'
    )
    st.altair_chart(chart, use_container_width=True)
    
elif chart_type == 'Pie Chart':
    fig_pie = px.pie(selected_data, names='항목', values='2022', title=f'{selected_region} 지역 2022년 학교급별 1인당 월평균 사교육비')
    st.plotly_chart(fig_pie, use_container_width=True)

elif chart_type == 'Scatter Plot':
    chart = alt.Chart(selected_data).mark_circle().encode(
        x='항목',
        y='2022',
        tooltip=['항목', '2022']
    ).properties(
        title=f'{selected_region} 지역 2022년 학교급별 1인당 월평균 사교육비 (Scatter Plot)'
    )
    st.altair_chart(chart, use_container_width=True)

elif chart_type == 'XY Heat map':
    chart = alt.Chart(selected_data).mark_rect().encode(
        x='항목',
        y='2022',
        color='2022',
        tooltip=['항목', '2022']
    ).properties(
        title=f'{selected_region} 지역 2022년 학교급별 1인당 월평균 사교육비 (XY Heat map)'
    )
    st.altair_chart(chart, use_container_width=True)
    
st.write(f'{selected_region} 지역의 2022년 학교급별 1인당 월평균 사교육비:')
st.write(selected_data)