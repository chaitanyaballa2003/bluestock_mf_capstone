import pandas as pd
import numpy as np

RF = 0.065

df = pd.read_csv("data/raw/02_nav_history.csv")

df = df.sort_values(["amfi_code", "date"])

df["daily_return"] = (
    df.groupby("amfi_code")["nav"]
    .pct_change()
)

results = []

for fund in df["amfi_code"].unique():

    returns = (
        df[df["amfi_code"] == fund]["daily_return"]
        .dropna()
    )

    downside = returns[returns < 0]

    annual_return = returns.mean() * 252
    downside_std = downside.std() * np.sqrt(252)

    sortino = (
        (annual_return - RF)
        / downside_std
    )

    results.append(
        [fund, round(sortino, 3)]
    )

sortino_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "sortino_ratio"
    ]
)

print(
    sortino_df.sort_values(
        "sortino_ratio",
        ascending=False
    ).head(10)
)