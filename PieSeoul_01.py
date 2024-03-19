import plotly.express as px
import pandas as pd
import plotly.io as pio

# 엑셀 파일 로드
df = pd.read_excel("./data/2022_서울_시군구별_자전거(피해운전자)_교통사고수.xls")

# 데이터 출력
print(df)
print("-" * 100)
print(df.head())


# 파이 차트 생성
fig = px.pie(data_frame=df,
            values='2022',
            names='시군구',
            template='plotly_dark')


# 파이 차트 스타일 및 레이아웃 설정
fig.update_traces(
    hole=.3,
    textposition = 'outside',
    textinfo= 'label+percent',
    textfont_color='white'
    )

# fig.update_layout(
    # title_text="2022년 서울 시군구별 자전거(피해운전자) 교통사고건수")

fig.update_layout(
                 title_x = 0.5,
                 title_xanchor = "auto",
                 title_yanchor = "auto",
                 title_font_size= 25)

# 툴팁 설정
fig.update_traces(hovertemplate='<b>%{label}</b> <br>'+
                                '사망자(수) : %{value}')

# # 그래프 표시
# fig.show()


# HTML 파일로 저장
fig.write_html("PieSeoul_01.html")