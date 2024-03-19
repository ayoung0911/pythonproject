import plotly.express as px
import pandas as pd

# 자전거 교통사고 통계 데이터를 DataFrame으로 생성
data = {
    '요일': ['일', '월', '화', '수', '목', '금', '토'],
    '사고건수': [848, 1130, 1138, 1151, 1207, 1273, 1130],
    '사망자수': [12, 15, 15, 16, 17, 12, 18],
    '부상자수': [908, 1151, 1158, 1178, 1242, 1317, 1188]
}
df = pd.DataFrame(data)

# 파이 차트 생성
fig = px.pie(df, values='사고건수', names='요일', title='자전거 교통사고 요일별 건수 분포')

# HTML 파일로 저장
fig.write_html("ex09.html")