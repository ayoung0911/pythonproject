import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 데이터 생성
df = pd.read_excel("./data/2022_연령층별_성별_부상자수.xls")

fig = go.Figure()

fig.add_trace(go.Funnel(
    name = '남',
    y = df['연령 '],
    x = df['남'],
    ))

fig.add_trace(go.Funnel(
    name = '여',
    y = df['연령 '],
    x = df['여'],
    ))

fig.update_layout(
    template='plotly_dark',
    title_text="2022년 자전거 사고 부상자수 (연령층별,성별)",
    title_x = 0.5,
    title_font_size = 40
    )

# HTML 파일로 저장
fig.write_html("FunnelChart_01.html")