import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

# Aggregate sector weights
sector_weights = (
    df.groupby("sector")["weight_pct"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,8))

plt.pie(
    sector_weights,
    labels=sector_weights.index,
    autopct="%1.1f%%",
    wedgeprops={"width": 0.4}
)

plt.title("Sector Allocation Across Equity Funds")

plt.show()