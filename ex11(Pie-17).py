import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

df = pd.read_excel("./data/Report10.xls")
print(df)


fig = go.Figure()

# Create subplots: use 'domain' type for Pie subplot
fig.add_trace(go.Pie(labels=df['도로구분별'],
                     values=df['발생건수 (건)'],
                     pull=[0, 0.2],
                     ))

fig.update_traces(hole=.4,
                #   textposition='outside',
                  textfont_size=15,
                  textinfo="label+percent")

fig.update_layout(
    template='plotly_dark',
    title_text="자전거도로 여부에 따른 자전거 교통사고",
    title_x = 0.5,
    title_font_size = 40
    )

fig.update_traces(
                  marker_line_color= "white",
                  marker_line_width = 2)

# HTML 파일로 저장
fig.write_html("ex11(Pie-17).html")