import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

results = []

for fund in df["amfi_code"].unique():

    fund_df = (
        df[df["amfi_code"] == fund]
        .sort_values("date")
    )

    running_max = fund_df["nav"].cummax()

    drawdown = (
        fund_df["nav"]
        / running_max
        - 1
    )

    max_dd = drawdown.min()

    results.append([
        fund,
        round(max_dd * 100, 2)
    ])

dd_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "max_drawdown_pct"
    ]
)

print(
    dd_df.sort_values(
        "max_drawdown_pct"
    ).head(10)
)
dd_df.to_csv(
    "data/processed/max_drawdown.csv",
    index=False
)

print("max_drawdown.csv saved successfully")