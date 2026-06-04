import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"])

results = []

for fund in df["amfi_code"].unique():

    fund_df = df[df["amfi_code"] == fund].sort_values("date")

    start_nav = fund_df.iloc[0]["nav"]
    end_nav = fund_df.iloc[-1]["nav"]

    years = (
        fund_df["date"].max() -
        fund_df["date"].min()
    ).days / 365

    cagr = (
        (end_nav / start_nav)
        ** (1 / years)
        - 1
    ) * 100

    results.append(
        [fund, round(cagr, 2)]
    )

cagr_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "cagr_percent"
    ]
)

print(cagr_df.head())

print("\nTop 10 Funds by CAGR")

print(
    cagr_df.sort_values(
        "cagr_percent",
        ascending=False
    ).head(10)
)
cagr_df.to_csv(
    "data/processed/cagr.csv",
    index=False
)

print("cagr.csv saved successfully")
cagr_df.to_csv(
    "data/processed/cagr.csv",
    index=False
)