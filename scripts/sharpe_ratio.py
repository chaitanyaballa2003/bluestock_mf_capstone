import pandas as pd
import numpy as np

RF = 0.065  # 6.5% risk-free rate

df = pd.read_csv("data/raw/02_nav_history.csv")

df = df.sort_values(["amfi_code", "date"])

df["daily_return"] = (
    df.groupby("amfi_code")["nav"]
    .pct_change()
)

results = []

for fund in df["amfi_code"].unique():

    fund_returns = (
        df[df["amfi_code"] == fund]["daily_return"]
        .dropna()
    )

    annual_return = fund_returns.mean() * 252
    annual_vol = fund_returns.std() * np.sqrt(252)

    sharpe = (
        (annual_return - RF)
        / annual_vol
    )

    results.append(
        [fund, round(sharpe, 3)]
    )

sharpe_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "sharpe_ratio"
    ]
)

print("\nTop 10 Funds by Sharpe Ratio")

print(
    sharpe_df.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(10)
)
sharpe_df.to_csv(
    "data/processed/sharpe_ratio.csv",
    index=False
)

print("sharpe_ratio.csv saved successfully")