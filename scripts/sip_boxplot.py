import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/08_investor_transactions.csv")

sip_df = df[df["transaction_type"] == "SIP"]

plt.figure(figsize=(10,5))

sns.boxplot(
    data=sip_df,
    x="age_group",
    y="amount_inr"
)

plt.title("SIP Amount Distribution by Age Group")

plt.show()