import requests
import os

# Resource URL for CSV file (example, update if needed)
RESOURCE_URL = "https://data.gov.hk/en-data/dataset/hk-censtatd-tablechart-110-01001/resource/091f3641-8404-4d9d-a5e3-05fcabe14a56/download/tablechart-110-01001.csv"
OUTPUT_PATH = "output/tablechart-110-01001.csv"

# Create output directory if it doesn't exist
os.makedirs("output", exist_ok=True)

print(f"Downloading CSV from {RESOURCE_URL} ...")
response = requests.get(RESOURCE_URL)
if response.status_code == 200:
    with open(OUTPUT_PATH, "wb") as f:
        f.write(response.content)
    print(f"Download complete. Saved to {OUTPUT_PATH}")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
