import webbrowser

import folium
from folium.plugins import HeatMap
import numpy as np
import pandas as pd

data = (
    np.random.normal(size=(50, 3)) * np.array([[1, 1, 1]]) + np.array([[48, 5, 1]])
).tolist()
print(data)

data1 = pd.read_csv('./data/자전거사고다발지역(서울).csv', encoding='euc-kr')
data2 = data1[['위도','경도','사고건수']]
data3 = []
for i, item in data2.iterrows():
    # print(i, item['위도'], item['경도'], item['사고건수'])
    data3.append([ item['위도'], item['경도'], item['사고건수']])
print(data3)

m = folium.Map([37.56, 127.00], zoom_start=11)
HeatMap(data3).add_to(m)
m.save('./ay_heatmap_seoul_01.html')
webbrowser.open_new("ay_heatmap_seoul_01.html")