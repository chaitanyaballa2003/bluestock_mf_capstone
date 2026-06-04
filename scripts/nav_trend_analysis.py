import pandas as pd
import plotly.express as px

df = pd.read_csv("data/raw/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"])

fig = px.line(
    df,
    x="date",
    y="nav",
    color="amfi_code",
    title="Daily NAV Trend of All Mutual Funds"
)

fig.show()