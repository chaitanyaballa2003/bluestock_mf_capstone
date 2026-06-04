import pandas as pd

# Load files
cagr = pd.read_csv("data/processed/cagr.csv")
sharpe = pd.read_csv("data/processed/sharpe_ratio.csv")
alpha = pd.read_csv("data/processed/alpha_beta.csv")
drawdown = pd.read_csv("data/processed/max_drawdown.csv")

# Merge
scorecard = (
    cagr
    .merge(sharpe, on="amfi_code")
    .merge(alpha[["amfi_code", "alpha"]], on="amfi_code")
    .merge(drawdown, on="amfi_code")
)

# Ranking
scorecard["cagr_rank"] = scorecard["cagr_percent"].rank(pct=True)
scorecard["sharpe_rank"] = scorecard["sharpe_ratio"].rank(pct=True)
scorecard["alpha_rank"] = scorecard["alpha"].rank(pct=True)

# Lower drawdown is better
scorecard["drawdown_rank"] = (
    scorecard["max_drawdown_pct"]
    .rank(pct=True, ascending=False)
)

# Composite Score (0–100)
scorecard["fund_score"] = (
      scorecard["cagr_rank"] * 30
    + scorecard["sharpe_rank"] * 25
    + scorecard["alpha_rank"] * 20
    + scorecard["drawdown_rank"] * 25
)

scorecard["fund_score"] = scorecard["fund_score"].round(2)

scorecard = scorecard.sort_values(
    "fund_score",
    ascending=False
)

print("\nTop 10 Funds")
print(
    scorecard[
        ["amfi_code", "fund_score"]
    ].head(10)
)

scorecard.to_csv(
    "data/processed/fund_scorecard.csv",
    index=False
)

print("\nfund_scorecard.csv saved successfully")