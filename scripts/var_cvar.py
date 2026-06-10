import pandas as pd

# Load NAV history
df = pd.read_csv("data/processed/02_nav_history.csv")

# Sort data
df = df.sort_values(["amfi_code", "date"])

results = []

for fund in df["amfi_code"].unique():

    fund_df = df[df["amfi_code"] == fund].copy()

    # Daily returns
    fund_df["daily_return"] = fund_df["nav"].pct_change()

    returns = fund_df["daily_return"].dropna()

    if len(returns) < 10:
        continue

    # VaR 95%
    var_95 = returns.quantile(0.05)

    # CVaR 95%
    cvar_95 = returns[returns <= var_95].mean()

    results.append([
        fund,
        round(var_95 * 100, 4),
        round(cvar_95 * 100, 4)
    ])

report = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "VaR_95_pct",
        "CVaR_95_pct"
    ]
)

print(report.head())

report.to_csv(
    "data/processed/var_cvar_report.csv",
    index=False
)

print("var_cvar_report.csv saved successfully")