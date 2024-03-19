import plotly.express as px
import pandas as pd
import plotly.io as pio
import numpy as np

# 엑셀 파일 로드
df = pd.read_excel("./data/2022_OECD_자전거_승차중_사망자수.xls")

# 데이터 출력
print(df)


# 트리맵 생성
fig = px.treemap(df,
                  path=[px.Constant("OECD 국가"),'국가'],
                  values='2020',
                  color='2020',
                  color_continuous_scale='RdBu')


# 레이아웃 설정
fig.update_layout(
    title_text="2022년 OECD 국가 자전거 승차중 사망자수"
    )


fig.update_layout(
    uniformtext=dict(minsize=10),
    margin = dict(t=50, l=10, r=10, b=10)
)

# 트리맵 스타일 및 텍스트 설정
fig.update_traces(marker=dict(cornerradius=5),
                  textinfo="label+value")

fig.update_layout(
                 title_x = 0.5,
                 title_xanchor = "auto",
                 title_yanchor = "auto",
                 title_font_size= 25)

fig.update_traces(hovertemplate='<b>%{label}</b> <br>'+
                                '사망자(수) : %{value}')

# # 그래프 표시
# fig.show()

# HTML 파일로 저장
fig.write_html("TreeMap_OECD_01.html")

