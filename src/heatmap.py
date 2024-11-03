import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Dashアプリの初期化
app = dash.Dash(__name__)

# データの作成
days = ['月', '火', '水', '木', '金', '土', '日']
hours = ['00:00', '06:00', '12:00', '18:00', '24:00']

# ランダムなデータを作成
data = np.random.randint(1, 10, size=(len(hours), len(days)))

# DataFrameに変換
df = pd.DataFrame(data, index=hours, columns=days)

# ヒートマップの作成
fig = go.Figure(data=go.Heatmap(
    z=df.values,
    x=df.columns,
    y=df.index,
    colorscale='Viridis',
    colorbar=dict(title='値'),
    text=df.values,  # 各セルの値を表示
    texttemplate="%{text:.0f}",  # 整数表示
    hoverinfo='text',  # ホバー時に値を表示
))

# Y軸の設定を離散値として表示
fig.update_layout(
    yaxis=dict(
        title='時間',
        tickvals=hours,  # 離散的なラベルを設定
        ticktext=hours   # 表示するラベルも同じ
    ),
    xaxis_title='曜日',
    title='曜日と時間の離散値ヒートマップ',
    showlegend=False
)

# 区切り線の追加
for i in range(1, len(days)):
    fig.add_shape(type='line',
                  x0=i - 0.5, x1=i - 0.5,
                  y0=-0.5, y1=len(hours) - 0.5,
                  line=dict(color='black', width=1))

for i in range(1, len(hours)):
    fig.add_shape(type='line',
                  x0=-0.5, x1=len(days) - 0.5,
                  y0=i - 0.5, y1=i - 0.5,
                  line=dict(color='black', width=1))

# ヒートマップ周囲の線を追加
fig.add_shape(type='line',
              x0=-0.5, x1=len(days) - 0.5,
              y0=-0.5, y1=-0.5,
              line=dict(color='black', width=2))  # 下側の線

fig.add_shape(type='line',
              x0=-0.5, x1=-0.5,
              y0=-0.5, y1=len(hours) - 0.5,
              line=dict(color='black', width=2))  # 左側の線

fig.add_shape(type='line',
              x0=len(days) - 0.5, x1=len(days) - 0.5,
              y0=-0.5, y1=len(hours) - 0.5,
              line=dict(color='black', width=2))  # 右側の線

fig.add_shape(type='line',
              x0=-0.5, x1=len(days) - 0.5,
              y0=len(hours) - 0.5, y1=len(hours) - 0.5,
              line=dict(color='black', width=2))  # 上側の線

# アプリのレイアウト
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

# アプリの実行
if __name__ == '__main__':
    app.run_server(debug=True)

