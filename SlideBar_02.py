import plotly.express as px
import pandas as pd
import plotly.io as pio
import numpy as np



# 엑셀 파일 로드
df = pd.read_excel("./data/2018~2022_월별_자전거(피해운전자)_교통사고수.xls")

# 데이터 출력
print(df)
print("-" * 100)
print(df.head())

# 바 차트 생성
fig = px.bar(df, y='구분값', x='기준월', text_auto='.2s',
            animation_frame="기준년도",
            color='기준월',
            color_continuous_scale='RdBu',
            template='plotly_dark'
            )


# Y축 설정
fig.update_yaxes(title_text='사고 수')


# 레이아웃 설정
fig.update_layout(
    title_text="월별 자전거(피해운전자) 교통사고수"
    )

fig.update_layout(
                 title_x = 0.5,
                 title_xanchor = "auto",
                 title_yanchor = "auto",
                 title_font_size= 25)

# fig.update_traces(hovertemplate='<b>%{x}</b> <br>'+
#                                 '%{xother}년 <br>' +
#                                 '사고(수) : %{y}')



# # 그래프 표시
# fig.show()

# HTML 파일로 저장
fig.write_html("SlideBar_02.html")