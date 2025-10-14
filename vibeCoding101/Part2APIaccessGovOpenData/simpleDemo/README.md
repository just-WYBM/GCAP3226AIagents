# How to Access the Hong Kong Census Tablechart Dataset via API

## Overview
This dataset provides population statistics and related data from the Hong Kong Census and Statistics Department. The data is available on data.gov.hk and can be accessed programmatically using the CKAN API.

## What Data is Available?
- Population statistics by year, age, gender, and other demographics
- Downloadable resources in CSV, XLS, and PDF formats
- Data dictionary for understanding field definitions
- Multiple resources linked from the main dataset page

## How to Retrieve Data via API

### Step 1: Find the Dataset
Go to: https://data.gov.hk/en-data/dataset/hk-censtatd-tablechart-110-01001

### Step 2: Identify Resource IDs
Each downloadable file (CSV, XLS, PDF) has a unique resource ID in the URL, e.g.:
- https://data.gov.hk/en-data/dataset/hk-censtatd-tablechart-110-01001/resource/091f3641-8404-4d9d-a5e3-05fcabe14a56

### Step 3: Use the CKAN API
The CKAN API allows you to fetch metadata and download resources. The main endpoints are:
- Get dataset info: `https://data.gov.hk/en-data/api/3/action/package_show?id=hk-censtatd-tablechart-110-01001`
- Get resource info: `https://data.gov.hk/en-data/api/3/action/resource_show?id=<resource_id>`
- Download resource: Use the direct resource URL

### Step 4: Example Pseudo Code

#### Fetch Dataset Metadata
```
1. Go to the API endpoint for the dataset:
   https://data.gov.hk/en-data/api/3/action/package_show?id=hk-censtatd-tablechart-110-01001
2. Read the JSON response to see available resources and metadata.
```

#### Download a Resource
```
1. Find the resource ID you want (from the dataset page or metadata).
2. Go to the resource URL, e.g.:
   https://data.gov.hk/en-data/dataset/hk-censtatd-tablechart-110-01001/resource/091f3641-8404-4d9d-a5e3-05fcabe14a56
3. Download the file (CSV, XLS, PDF) directly from your browser or using a tool like Excel or Google Sheets.
```

#### For Non-Programmers
- You can copy and paste the resource URLs into your browser to download files.
- Use Excel or Google Sheets to open CSV/XLS files.
- The API endpoints above can be used in simple tools or scripts if you want to automate downloads.

## Useful Links
- [CKAN API Documentation](https://data.gov.hk/en/help/api-spec)
- [CKAN API Development Guide](https://data.gov.hk/en/help/ckan-api-development-guide)
- [Data Dictionary (PDF)](https://www.censtatd.gov.hk/datagovhk/WT_data_dict_en.pdf)

## Notes
- Some resources may require you to check the data dictionary for field definitions.
- The API is open and does not require authentication for public datasets.

---
This guide helps you understand what data is available and how to retrieve it using simple steps and pseudo code. For more advanced automation, refer to the CKAN API documentation above.
