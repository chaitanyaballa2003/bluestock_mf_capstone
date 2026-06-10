import pandas as pd

scorecard = pd.read_csv(
    "data/processed/fund_scorecard.csv"
)

top_funds = (
    scorecard
    .sort_values(
        "fund_score",
        ascending=False
    )
    .head(3)
)

print("Recommended Funds")
print(top_funds)

top_funds.to_csv(
    "data/processed/recommended_funds.csv",
    index=False
)

print(
    "recommended_funds.csv saved successfully"
)