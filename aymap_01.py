import plotly.express as px
import pandas as pd

df = pd.read_csv('./data/공공자전거 대여소 정보(23.06월 기준).csv', encoding='euc-kr')
print(df)

fig = px.scatter_mapbox(df,  # 데이터 전체
                        lat="위도",
                        lon="경도", 
                        color='자치구',
                        hover_name="대여소명",
                        size='거치대수',
                        color_continuous_scale=px.colors.cyclical.IceFire,                      
                        size_max=25, 
                        zoom=10)

# 스타일을 지정하지 않으면 지도가 보이지 않는다.
fig.update_layout(mapbox_style="open-street-map")

# HTML 파일로 저장
fig.write_html("aymap_01.html")