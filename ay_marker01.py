# folium.Map(location=[위도, 경도], zoom_start=지도 배율)
import webbrowser

import pandas as pd
from folium import folium
from folium.features import Icon, CustomIcon, Tooltip, Popup, Marker
from folium.plugins import MarkerCluster

lat, lon = 37.54060, 126.8368
my_map = folium.Map(location=[lat, lon], zoom_start=6.5)
marker_cluster = MarkerCluster().add_to(my_map)

bicycle = pd.read_csv('./data/공공자전거 대여소 정보(23.06월 기준).csv', encoding='euc-kr')
for i, row in bicycle.iterrows():
       Marker(location=[row['위도'], row['경도']],
              tooltip="주소: " + row['주소'],
              popup=Popup("대여소명: " + str(row['대여소명']) + "<br>" + "거치대수: " + str(row['거치대수']), max_width=100),
              icon=CustomIcon('./data/bicycle100.png', icon_size=(100, 100))).add_to(marker_cluster)
 
my_map.save('ay_marker01.html')
# webbrowser.open("ay_marker_01.html")
