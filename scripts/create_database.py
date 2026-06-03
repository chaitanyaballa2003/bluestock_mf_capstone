import pandas as pd
import os
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///data/db/bluestock_mf.db")

processed_path = "data/processed"

files = [f for f in os.listdir(processed_path) if f.endswith(".csv")]

print("Total Files:", len(files))

for file in files:

    table_name = file.replace(".csv", "")

    print(f"Loading {table_name}...")

    df = pd.read_csv(
        os.path.join(processed_path, file)
    )

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

print("\nDatabase created successfully!")
print("Location: data/db/bluestock_mf.db")