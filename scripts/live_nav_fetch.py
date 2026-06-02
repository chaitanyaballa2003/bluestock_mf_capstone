import requests
import pandas as pd 
url = "https://api.mfapi.in/mf/125497"
response = requests.get(url)
data = response.json()
print("Scheme Name:", data["meta"]["scheme_name"])
nav_df = pd.DataFrame(data["data"])
print(nav_df.head())
nav_df.to_csv(
    "data/raw/hdfc_top100_nav.csv",
    index=False
)
print("CSV file saved successfully")