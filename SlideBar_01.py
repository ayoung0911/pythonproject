import plotly.express as px
import pandas as pd
import plotly.io as pio
import numpy as np

# 엑셀 파일 로드
df = pd.read_excel("./data/2022_전국_자전거(피해운전자)_교통사고수.xls")

# 데이터 출력
print(df)
print("-" * 100)
print(df.head())


# Bar 차트 생성
fig = px.bar(df, y='2022', x='시군구', text_auto='.2s',
            animation_frame="시도",
            color='2022',
            color_continuous_scale='RdBu',
            template='plotly_dark'
            )


# Y축 범위 설정
fig.update_yaxes(range=[0, 250])
fig.update_yaxes(title_text='사고 수')

# 레이아웃 설정
fig.update_layout(
    title_text="2022년 전국 자전거(피해운전자) 교통사고 건수"
    )

fig.update_layout(
                 title_x = 0.5,
                 title_y = 0.9,
                 title_xanchor = "center",
                 title_yanchor = "middle",
                 title_font_size= 25)


# # 그래프 표시
# fig.show()

# HTML 파일로 저장
fig.write_html("SlideBar_01.html")