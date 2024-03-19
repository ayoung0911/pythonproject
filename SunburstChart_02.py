
import plotly.express as px
import pandas as pd

# 엑셀 파일 로드
df = pd.read_excel("./data/2022_전국_자전거(피해운전자)_교통사고수.xls")

# Sunburst 차트 생성
fig = px.sunburst(df,
                  path=['시도', '시군구'],
                  values='2022',
                  color='2022',
                  color_continuous_scale='RdBu',
                  hover_name='시도',
                  template='plotly_dark')

# 레이아웃 및 스타일 설정
fig.update_layout(
    title_text="전국 자전거(피해운전자) 교통사고 2022년 사고건수",
    title_y=0.95,  # 기본값은 1
    title_x=0.5,
    title_xanchor='center',
    title_yanchor='middle',  # middle로 조정하여 중앙으로 이동
    title_font_size=25,
    title_font_color="White",
    title_font_family="Times",
    margin=dict(t=70)  # 여기서 조절 가능
)

fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')

# 툴팁 설정
fig.update_traces(hovertemplate='<b>%{label}</b> <br>' +
                                '사고수 : %{value}')

# HTML 파일로 저장
fig.write_html("SunburstChart_02.html")
