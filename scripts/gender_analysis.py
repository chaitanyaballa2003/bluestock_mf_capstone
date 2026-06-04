import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/08_investor_transactions.csv")

gender_counts = df["gender"].value_counts()

plt.figure(figsize=(6,4))
gender_counts.plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Investors")

plt.show()