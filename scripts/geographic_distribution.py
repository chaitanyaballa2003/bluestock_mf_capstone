import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# State-wise SIP Amount
state_sip = df.groupby("state")["amount_inr"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
state_sip.head(10).plot(kind="barh")

plt.title("Top 10 States by Investment Amount")
plt.xlabel("Investment Amount (INR)")
plt.ylabel("State")

plt.show()

# T30 vs B30 Pie Chart
plt.figure(figsize=(6,6))

df["city_tier"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("T30 vs B30 Distribution")
plt.ylabel("")

plt.show()