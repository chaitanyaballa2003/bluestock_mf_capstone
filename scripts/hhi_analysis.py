import pandas as pd

df = pd.read_csv(
    "data/processed/09_portfolio_holdings.csv"
)

results = []

for fund in df["amfi_code"].unique():

    temp = df[
        df["amfi_code"] == fund
    ]

    hhi = (
        (temp["weight_pct"] / 100) ** 2
    ).sum()

    results.append([
        fund,
        round(hhi, 4)
    ])

report = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "HHI"
    ]
)

print(report.head())

report.to_csv(
    "data/processed/hhi_report.csv",
    index=False
)

print("hhi_report.csv saved successfully")