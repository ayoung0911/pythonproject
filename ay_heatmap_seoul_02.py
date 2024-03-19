import pandas as pd
import plotly.express as px

# 데이터 불러오기
df = pd.read_csv('./data/자전거사고다발지역(서울).csv', encoding='euc-kr')

# 밀도 맵 그리기
import plotly.express as px
fig = px.density_mapbox(df, lat='위도', lon='경도', z='사고건수', radius=15,
                        center=dict(lat=37.56, lon= 127.00), zoom=10.5,
                        mapbox_style="open-street-map")

# HTML 파일로 저장
fig.write_html("ay_heatmap_seoul_02.html")