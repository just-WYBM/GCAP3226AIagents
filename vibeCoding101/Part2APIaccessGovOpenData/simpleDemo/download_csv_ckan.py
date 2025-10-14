import requests
import os

# CKAN API endpoint for dataset metadata
DATASET_ID = "hk-censtatd-tablechart-110-01001"
API_URL = f"https://data.gov.hk/en-data/api/3/action/package_show?id={DATASET_ID}"
OUTPUT_PATH = "output/tablechart-110-01001.csv"

# Create output directory if it doesn't exist
os.makedirs("output", exist_ok=True)

print(f"Fetching dataset metadata from {API_URL} ...")
response = requests.get(API_URL)
if response.status_code == 200:
    data = response.json()
    resources = data['result']['resources']
    # Try to find a CSV resource
    csv_resource = None
    for r in resources:
        if r.get('format', '').lower() == 'csv':
            csv_resource = r
            break
    if csv_resource:
        csv_url = csv_resource['url']
        print(f"Downloading CSV from {csv_url} ...")
        csv_response = requests.get(csv_url)
        if csv_response.status_code == 200:
            with open(OUTPUT_PATH, "wb") as f:
                f.write(csv_response.content)
            print(f"Download complete. Saved to {OUTPUT_PATH}")
        else:
            print(f"Failed to download CSV file. Status code: {csv_response.status_code}")
    else:
        print("No CSV resource found in dataset metadata.")
else:
    print(f"Failed to fetch dataset metadata. Status code: {response.status_code}")
