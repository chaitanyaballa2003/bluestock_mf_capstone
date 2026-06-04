import pandas as pd
from scipy.stats import linregress

# NAV data
df = pd.read_csv("data/raw/02_nav_history.csv")

df = df.sort_values(["amfi_code", "date"])

df["daily_return"] = (
    df.groupby("amfi_code")["nav"]
    .pct_change()
)

# Use average return of all funds as proxy benchmark
benchmark = (
    df.groupby("date")["daily_return"]
    .mean()
)

results = []

for fund in df["amfi_code"].unique():

    fund_df = df[df["amfi_code"] == fund]

    merged = pd.DataFrame({
        "fund": fund_df["daily_return"],
        "benchmark": benchmark.reindex(fund_df["date"]).values
    }).dropna()

    if len(merged) > 50:

        beta, alpha, r, p, std_err = linregress(
            merged["benchmark"],
            merged["fund"]
        )

        alpha = alpha * 252

        results.append([
            fund,
            round(alpha, 4),
            round(beta, 4)
        ])

alpha_beta_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "alpha",
        "beta"
    ]
)

print(alpha_beta_df.head())

alpha_beta_df.to_csv(
    "data/processed/alpha_beta.csv",
    index=False
)

print("\nalpha_beta.csv saved successfully")