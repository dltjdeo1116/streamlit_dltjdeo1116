import streamlit as st
import pandas as pd
import plotly.express as px

# 내가 주어진 데이터
data = pd.read_csv('data/학교급 및 시도별 학생 1인당 월평균 사교육비.csv', encoding='cp949')

# 내가 주어진 '값'
custom_values = [59.6, 39.5, 43.7, 38.6, 35.6, 38.9, 36.7]

# 위치 데이터 예제
location_data = pd.DataFrame({
    '시도별': ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시'],
    '위도': [37.5665, 35.1796, 35.8714, 37.4538, 35.1595, 36.3504, 35.5384],
    '경도': [126.9780, 129.0756, 128.6014, 126.7317, 126.8526, 127.3845, 129.3114],
    '값': custom_values  # 'Field Map'에서 사용할 값
})

# 대한민국 지도 경계선 데이터 (GeoJSON 형식, 실제 데이터로 대체해야 함)
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature", "properties": {"name": "서울특별시"}, "geometry": {"type": "Polygon", "coordinates": [[[124.5658, 38.1057], [131.8682, 38.1057], [131.8682, 33.0981], [124.5658, 33.0981], [124.5658, 38.1057]]]}}
    ]
}

# 각 지역별로 2022년 학생 1인당 월평균 사교육비의 값 계산
average_data = data.groupby('시도별')['2022'].mean().reset_index()

# Streamlit 애플리케이션 시작
st.title('지도 시각화 - 2022년 학생 1인당 월평균 사교육비의 지역별 평균값 및 위치 데이터')

fig_symbol_map = px.scatter_mapbox(
    location_data,
    lat='위도',
    lon='경도',
    text='시도별',
    size='값',
    mapbox_style='carto-positron',
    center={'lat': 36.5, 'lon': 127.5},
    zoom=6,
    title='지역별 2022년 학생 1인당 월평균 사교육비의 평균값 (Symbol Map)'
)
st.plotly_chart(fig_symbol_map, use_container_width=True)

# 'XY Tree Map'
fig_xy_tree_map = px.treemap(
    location_data,
    path=['시도별'],
    values='값',
    title='XY Tree Map'
)
st.plotly_chart(fig_xy_tree_map, use_container_width=True)
