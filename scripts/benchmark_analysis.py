# scripts/benchmark_analysis.py

import pandas as pd

df = pd.read_csv("data/raw/10_benchmark_indices.csv")

print(df.head())
print("\nColumns:")
print(df.columns)