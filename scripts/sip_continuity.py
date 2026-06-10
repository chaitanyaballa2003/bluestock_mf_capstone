import pandas as pd

df = pd.read_csv("data/processed/08_investor_transactions.csv")

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

df = df.sort_values(
    ["investor_id", "transaction_date"]
)

results = []

for investor in df["investor_id"].unique():

    temp = df[
        df["investor_id"] == investor
    ].copy()

    temp["gap_days"] = (
        temp["transaction_date"]
        .diff()
        .dt.days
    )

    avg_gap = temp["gap_days"].mean()

    at_risk = avg_gap > 35

    results.append([
        investor,
        round(avg_gap, 2)
        if pd.notna(avg_gap)
        else 0,
        at_risk
    ])

report = pd.DataFrame(
    results,
    columns=[
        "investor_id",
        "avg_gap_days",
        "at_risk"
    ]
)

print(report.head())

report.to_csv(
    "data/processed/sip_continuity_report.csv",
    index=False
)

print(
    "sip_continuity_report.csv saved successfully"
)