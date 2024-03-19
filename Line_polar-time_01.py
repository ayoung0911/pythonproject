import plotly.express as px
import pandas as pd

# 데이터 생성
df = pd.read_excel("./data/2022_시간대별_자전거(피해운전자)_교통사고_건수.xls")

#그래프 그리기
fig = px.line_polar(df, r="구분값",
                    theta="사고시간대",
                    line_close=True,
                    template='plotly_dark',
                    )

# 내부 색칠하기
fig.update_traces(fill='toself')

fig.update_layout(
    # title_text="2022년 시간대별 자전거(피해운전자) 교통사고건수",
    title_x=0.5,
    title_y=0.98,  # 조정된 값
    title_xanchor="center",
    title_yanchor="middle",
    title_font_size=25
)

fig.update_traces(hovertemplate='<b>사고시간대: %{theta}</b> <br>'+
                                '사고수: %{r}')

fig.update_layout(
    polar = dict(
      radialaxis_tickangle = 90,
      radialaxis_angle = 90)
      )


# HTML 파일로 저장
fig.write_html("Line_polar-time_01.html")
