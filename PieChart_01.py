import plotly.express as px
import pandas as pd
import plotly.io as pio

df = pd.read_excel("./data/2022_서울_시군구별_자전거(피해운전자)_교통사고수.xls")
print(df)
print("-" * 100)

print(df.head())

fig = px.pie(data_frame=df,
            values='2022',
            names='시군구',
            template='plotly_white')

fig.update_traces(
    hole=.3,
    textposition = 'outside',
    textinfo= 'label+percent',
    textfont_color='black'
    )

fig.update_layout(
    title_text="자전거(피해운전자) 교통사고 서울 시군구별 사고량")

# fig.show()


# HTML 파일로 저장
fig.write_html("PieChart_01.html")