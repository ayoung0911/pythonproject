import folium
from folium.features import Icon, CustomIcon, Tooltip, Popup, Marker
import requests
import json
import pandas as pd

# 서울 json 파일 읽어오기
geo_file = './seoul.geojson'
geo = json.load(open(geo_file, encoding='utf-8'))

# 위도 경도 지정
m = folium.Map(
    location=[37.559819, 126.963895],
    zoom_start=12, 
)

folium.GeoJson(
    geo,
    name='지역구'
).add_to(m)

# 데이터 파일 읽어오기
bicycle = pd.read_csv('./data/공공자전거 대여소 정보(23.06월 기준).csv', encoding='euc-kr')
data = bicycle[['대여소명','위도','경도','주소','거치대수']]
print(type(data)) 
for index, row in data.iterrows():
    print(index, " :", type(row), "(", row[0], ",",row[1],")")
    print("-" * 100)
    # 클릭시 나오게 하기
    popup = folium.Popup("대여소명: "+ row[0]+ "<br>" + "거치대수: " + str(row[4]), max_width=200)  
    folium.Marker(location=[row[1], row[2]], popup=popup, tooltip=row[3],
    icon=Icon(icon="bicycle", prefix="fa", color="lightred")).add_to(m)

# 지도맵 html 생성
m.save("ay_marker02.html")