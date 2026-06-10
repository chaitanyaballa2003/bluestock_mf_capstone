import pandas as pd

df = pd.read_csv(
    r"C:\Users\chait\bluestock_mf_capstone\data\processed\08_investor_transactions.csv"
)
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

first_txn = (
    df.groupby("investor_id")["transaction_date"]
    .min()
    .reset_index()
)

first_txn["cohort_year"] = first_txn["transaction_date"].dt.year

cohort_df = df.merge(
    first_txn[["investor_id", "cohort_year"]],
    on="investor_id"
)

report = (
    cohort_df.groupby("cohort_year")
    .agg(
        total_invested=("amount_inr", "sum"),
        avg_investment=("amount_inr", "mean"),
        investors=("investor_id", "nunique")
    )
    .reset_index()
)

print(report)

report.to_csv(
    "data/processed/cohort_analysis.csv",
    index=False
)

print("cohort_analysis.csv saved successfully")