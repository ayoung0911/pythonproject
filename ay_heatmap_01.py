import webbrowser
import folium
from folium.plugins import HeatMap
import numpy as np
import pandas as pd


# 랜덤 데이터 생성
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[48, 5, 1]])
).tolist()

# CSV 파일에서 데이터 읽어오기
data1 = pd.read_csv('./data/자전거사고다발지역.csv', encoding='euc-kr')
data2 = data1[['위도','경도','사고건수']]
data3 = []
for i, item in data2.iterrows():
    data3.append([ item['위도'], item['경도'], item['사고건수']])

# 지도 생성 
m = folium.Map([36.00, 126.98], zoom_start=7)

# 히트맵 생성 및 추가
HeatMap(data3).add_to(m)

# 지도를 HTML 파일로 저장 및 웹 브라우저에서 열기
m.save('./ay_heatmap_01.html')
webbrowser.open_new("ay_heatmap_01.html")