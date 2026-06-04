import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Sort data
df = df.sort_values(["amfi_code", "date"])

# Daily Return
df["daily_return"] = (
    df.groupby("amfi_code")["nav"]
    .pct_change()
)

print(df.head(10))

print("\nDaily Return Statistics:")
print(df["daily_return"].describe())