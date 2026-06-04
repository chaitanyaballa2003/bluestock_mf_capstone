import pandas as pd
import matplotlib.pyplot as plt

# Fund NAV Data
fund_df = pd.read_csv("data/raw/02_nav_history.csv")

# Benchmark Data
bench_df = pd.read_csv("data/raw/10_benchmark_indices.csv")

fund_df["date"] = pd.to_datetime(fund_df["date"])
bench_df["date"] = pd.to_datetime(bench_df["date"])

# Select top 5 funds from scorecard
top_funds = [120505, 148569, 100033, 148567, 120843]

plt.figure(figsize=(12,6))

for fund in top_funds:

    temp = (
        fund_df[fund_df["amfi_code"] == fund]
        .sort_values("date")
    )

    normalized = (
        temp["nav"] /
        temp["nav"].iloc[0]
    ) * 100

    plt.plot(
        temp["date"],
        normalized,
        label=f"Fund {fund}"
    )

# NIFTY 50
nifty50 = (
    bench_df[
        bench_df["index_name"] == "NIFTY50"
    ]
    .sort_values("date")
)

nifty50_norm = (
    nifty50["close_value"]
    / nifty50["close_value"].iloc[0]
) * 100

plt.plot(
    nifty50["date"],
    nifty50_norm,
    linewidth=3,
    label="NIFTY50"
)

plt.title(
    "Top 5 Funds vs NIFTY50"
)

plt.xlabel("Date")
plt.ylabel("Normalized Performance")

plt.legend()

plt.show()