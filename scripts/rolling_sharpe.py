import pandas as pd
import matplotlib.pyplot as plt

# Load NAV data
df = pd.read_csv("data/processed/02_nav_history.csv")

df = df.sort_values(["amfi_code", "date"])

top_funds = df["amfi_code"].unique()[:5]

plt.figure(figsize=(12,6))

for fund in top_funds:

    fund_df = df[df["amfi_code"] == fund].copy()

    fund_df["daily_return"] = fund_df["nav"].pct_change()

    fund_df["rolling_sharpe"] = (
        fund_df["daily_return"].rolling(90).mean()
        /
        fund_df["daily_return"].rolling(90).std()
    ) * (252 ** 0.5)

    plt.plot(
        fund_df["date"],
        fund_df["rolling_sharpe"],
        label=str(fund)
    )

plt.title("90-Day Rolling Sharpe Ratio")
plt.xlabel("Date")
plt.ylabel("Sharpe Ratio")
plt.legend()

plt.tight_layout()

plt.savefig(
    "data/processed/rolling_sharpe_chart.png"
)

print("rolling_sharpe_chart.png saved successfully")