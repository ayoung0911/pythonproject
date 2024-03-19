import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 엑셀 파일 읽기
df = pd.read_excel('./data/자전거도로시도별현황2022.xlsx')

# 데이터 설정
regions = df['시도별'].unique().tolist()
bike_paths = ['자전거전용도로', '자전거보행자겸용도로', '자전거전용차로', '자전거우선도로']
distances_by_region = []

# 각 지역별로 거리 데이터 가져오기
for region in regions:
    distances = []
    for path in bike_paths:
        distance = df.loc[df['시도별'] == region, path].values[0]
        distances.append(distance)
    distances_by_region.append(distances)

# 바 그래프 생성
fig = go.Figure()

# 각 막대의 색상을 지정하여 그래프에 추가
for i, bike_path in enumerate(bike_paths):
    fig.add_trace(
        go.Bar(name=bike_path, x=regions, y=[distances[i] for distances in distances_by_region],
               marker_color=['blue', 'purple', 'red', 'orange'][i])  # 바의 색상 직접 지정
    )

# 그래프 레이아웃 설정
fig.update_layout(
    title='시도별 자전거 도로 길이 (2022년)',
    xaxis=dict(title='시도별'),
    yaxis=dict(title='길이 (km)'),
    barmode='group',
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    autosize=True
)

# HTML 파일로 저장
fig.write_html("ay_bicycle01.html")
