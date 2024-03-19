import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import plotly.io as pio
import seaborn as sns

# 엑셀 파일 로드
df = pd.read_excel('./data/2018~2022_전국_자전거(피해운전자)_교통사고_건수.xls')

# Figure 객체 생성
fig = go.Figure()

# 각 연도에 대한 바 그래프 추가
fig.add_trace(
    go.Bar(
        name='2018년',
        x=df['시도'],
        y=df['2018'],
        text=df["2018"],
        # marker_color=df['2018'],
        # marker_colorscale = "aggrnyl",
        ))

fig.add_trace(
    go.Bar(
        name='2019년',
        x=df['시도'],
        y=df['2019'],
        text=df['2019'],
            ))

fig.add_trace(
    go.Bar(
        name='2020년',
        x=df['시도'],
        y=df['2020'],
        text=df['2020'],
            ))

fig.add_trace(
    go.Bar(
        name='2021년',
        x=df['시도'],
        y=df['2021'],
        text=df['2021'],
            ))

fig.add_trace(
    go.Bar(
        name='2022년',
        x=df['시도'],
        y=df['2022'],
        text=df['2022'],
            ))

# 바 그래프 스타일 설정
fig.update_traces(
    textfont_size = 14,
    textangle = 0,
    textposition = "outside",
    )

# 버튼 설정
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            buttons=list([
                dict(label="모두보기",
                     method="update",
                     args=[{"visible": [True, True, True, True, True]},
                           {"title": "자전거(피해운전자) 교통사고"}]),
                dict(label="2018년",
                     method="update",
                     args=[{"visible": [True, False, False, False, False]},
                           {"title": "2018년",}]),
                dict(label="2019년",
                     method="update",
                     args=[{"visible": [False, True, False, False, False]},
                           {"title": "2019년",}]),
                dict(label="2020년",
                     method="update",
                     args=[{"visible": [False, False, True, False, False]},
                           {"title": "2020년",}]),
                dict(label="2021년",
                     method="update",
                     args=[{"visible": [False, False, False, True, False]},
                           {"title": "2021년",}]),
                dict(label="2022년",
                     method="update",
                     args=[{"visible": [False, False, False, False, True]},
                           {"title": "2022년",}]),
            ]),
        ),
    ]
)


fig.update_layout(
    template='plotly_white',
    title_text="전국 자전거(피해운전자) 교통사고 사고건수",
    title_x = 0.5,
    title_font_size = 40
    )

# X축, Y축 설정
fig.update_xaxes(
    title_text='지역',
    title_font_size=30
)
fig.update_yaxes(
    range=[0, 10000],
    title_text='사고건수',
    title_font_size=30
    )

fig.update_layout(template='seaborn')

# # 그래프 표시
# fig.show()

# HTML 파일로 저장
fig.write_html("BarChart_02.html")