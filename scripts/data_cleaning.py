import pandas as pd
import os

raw_path = "data/raw"
processed_path = "data/processed"

files =[f for f in os.listdir(raw_path)if f.endswith(".csv")]
print("Total Files:", len(files))

for file in files:
    print("/n" + "=", len(files))
    print("Cleaning:", file)

    df = pd.read_csv(os.path.join(raw_path,file))
    print("Original Shape:", df.shape)

    df = df.drop_duplicates()

    print("After Cleaning:", df.shape)

    df.to_csv(
        os.path.join(processed_path, file),
        index=False
    )
print("\nAll files cleaned and saved successfully!")