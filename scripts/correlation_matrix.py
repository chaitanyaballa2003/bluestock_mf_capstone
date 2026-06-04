import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/02_nav_history.csv")

# Select 10 funds
top_funds = df["amfi_code"].unique()[:10]

df = df[df["amfi_code"].isin(top_funds)]

# Pivot table
pivot_df = df.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

# Daily returns
returns = pivot_df.pct_change().dropna()

# Correlation matrix
corr_matrix = returns.corr()

plt.figure(figsize=(10,8))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("NAV Return Correlation Matrix")

plt.show()