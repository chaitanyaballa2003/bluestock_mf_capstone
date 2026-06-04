import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

df["date"] = pd.to_datetime(df["date"])

df["year"] = df["date"].dt.year

plt.figure(figsize=(12,6))

sns.barplot(
    data=df,
    x="year",
    y="aum_lakh_crore",
    hue="fund_house"
)

plt.title("AUM Growth by Fund House")
plt.xlabel("Year")
plt.ylabel("AUM (Lakh Crore)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()