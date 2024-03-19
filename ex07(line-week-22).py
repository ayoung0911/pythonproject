import plotly.express as px
import pandas as pd
import plotly.io as pio
import numpy as np

df = pd.read_excel("./data/Report6.xls")
print(df.head())

fig = px.line(df, x="기준년도",
              y="구분값",
              color='사고요일',
              template='plotly_dark',
              text='구분값',
              symbol="사고요일")

fig.update_layout(
    title_text="2022년 요일별 자전거(피해운전자) 교통사고 부상자수"
    )

fig.update_layout(
                 title_x = 0.5,
                 title_xanchor = "center",
                 title_yanchor = "middle",
                 title_font_size= 25)

fig.update_xaxes(ticks="outside", dtick=1)

fig.update_traces(textposition="top center")

fig.update_traces(line_width=2)

fig.update_yaxes(title_text='부상자수')

fig.update_xaxes(title_font_size =30,
                 title_font_color='white',
                 title_font_family='Courier')
fig.update_yaxes(title_font_size =30,
                 title_font_color='white',
                 title_font_family='Courier')


# HTML 파일로 저장
fig.write_html("ex07(line-week-22).html")