import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import plotly.io as pio
import seaborn as sns
from datetime import datetime


# 최종

# 데이터 로드
df = pd.read_excel('./data/2018~2022_월별_교통사고_건수.xls')

# Figure 객체 생성
fig = go.Figure()

# Bar 그래프 추가
for year in df.columns[1:]:
    fig.add_trace(go.Bar(
        name=year,
        x=df['자전거피해운전자수'],
        y=df[year],
        text=df[year],
    ))

# Bar 그래프 스타일 설정
fig.update_traces(
    textfont_size=14,
    textangle=0,
    textposition="outside",
)

# 중복되는 년도 추출
unique_years = sorted(set(year[:4] for year in df.columns[1:]))

# 레이아웃 설정
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            buttons=[
                dict(label="모두보기",
                     method="update",
                     args=[{"visible": [True] * len(df.columns[1:])},
                           {"title": "자전거(피해운전자) 교통사고 건수"}]),
            ] + [
                dict(label=f"{year}년",
                     method="update",
                     args=[{"visible": [col[:4] == year for col in df.columns[1:]]},
                           {"title": f"교통사고 건수 <br> ▶{year}년◀"}])
                for year in unique_years
            ],   
        ),
    ],
    sliders=[dict(
        active=0,
        steps=[
            dict(
                method="update",
                args=[{"visible": [col == month for col in df.columns[1:]]},
                      {"title": f"교통사고 건수 <br> ▶{month}◀"}],
                label=f"{month[:4]}년{month[4:]}월" if month[4:] else f"{month[:4]}년"
            ) for month in df.columns[1:]
        ],
        pad={"t": 50},
        currentvalue=dict(
            visible=True,
            suffix="",
            font=dict(size=20),
        ),
    )],
    template='plotly_white',
    title_text="자전거(피해운전자)<br>월별 교통사고 건수",
    title_x=0.5,
    title_font_size=40,
)

# X축 설정
fig.update_xaxes(
    title_text='자전거피해운전자수',
    title_font_size=30
)

# Y축 설정
fig.update_yaxes(
    range=[0, 10000],
    title_font_size=20
)

# # 그래프 표시
# fig.show()

# HTML 파일로 저장
fig.write_html("BarChart_01.html")






# # 데이터 로드
# df = pd.read_excel('최근5년월별교통사고건수2.xls')

# # Figure 객체 생성
# fig = go.Figure()

# # Bar 그래프 추가
# for year in df.columns[1:]:
#     fig.add_trace(go.Bar(
#         name=year + '년',
#         x=df['자전거피해운전자수'],
#         y=df[year],
#         text=df[year],
#     ))

# # Bar 그래프 스타일 설정
# fig.update_traces(
#     textfont_size=14,
#     textangle=0,
#     textposition="outside",
# )

# # 중복되는 년도 추출
# unique_years = sorted(set(year[:4] for year in df.columns[1:]))

# # 레이아웃 설정
# fig.update_layout(
#     updatemenus=[
#         dict(
#             type="buttons",
#             buttons=[
#                 dict(label="모두보기",
#                      method="update",
#                      args=[{"visible": [True] * len(df.columns[1:])},
#                            {"title": "자전거(피해운전자) 교통사고 건수"}]),
#             ] + [
#                 dict(label=f"{year}년",
#                      method="update",
#                      args=[{"visible": [col[:4] == year for col in df.columns[1:]]},
#                            {"title": f"교통사고 건수 <br> ▶{year}년◀"}])
#                 for year in unique_years
#             ],
#         ),
#     ],
#     sliders=[dict(
#         active=0,
#         steps=[
#             dict(
#                 method="update",
#                 args=[{"visible": [col == month for col in df.columns[1:]]},
#                       {"title": f"교통사고 건수 <br> ▶{month}◀"}],
#                 label=f"{int(month[:4])}년{int(month[4:]):02d}월"
#             ) for month in df.columns[1:]
#         ],
#         pad={"t": 50},
#         currentvalue=dict(
#             visible=True,
#             suffix="",
#             font=dict(size=20),
#         ),
#     )],
#     template='plotly_white',
#     title_text="자전거(피해운전자) 교통사고 건수",
#     title_x=0.5,
#     title_font_size=40,
# )

# # X축 설정
# fig.update_xaxes(
#     title_text='자전거피해운전자수',
#     title_font_size=30
# )

# # Y축 설정
# fig.update_yaxes(
#     range=[0, 10000],
#     title_font_size=20
# )

# # 그래프 표시
# fig.show()

