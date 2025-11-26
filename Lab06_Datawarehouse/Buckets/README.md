# Lab 06 - Part 1: Google Cloud Storage (GCS) Setup

## Overview
This lab demonstrates how to set up Google Cloud Storage (GCS) for data warehousing purposes. GCS provides scalable and secure cloud storage that integrates seamlessly with BigQuery for data analysis.

---

## What is Google Cloud Storage (GCS)?
Google Cloud Storage (GCS) is a fully-managed, scalable storage service that allows you to store any type of data in the cloud. It serves as the foundation for data pipelines and integrates with other Google services like BigQuery, Machine Learning, and more.

---

## Lab Objectives
- Create a GCS bucket for data warehousing
- Upload a dataset to the bucket
- Enable object versioning for data recovery
- Prepare data for BigQuery integration

---

## Prerequisites
- Active Google Cloud Platform (GCP) account
- GCP project with billing enabled
- Dataset file ready for upload (CSV format recommended)

---

## Step 1: Create a GCS Bucket

### Using Google Cloud Console (Web Interface):

1. **Navigate to Google Cloud Console**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Ensure you're in the correct project with billing enabled

2. **Access Cloud Storage**:
   - Click the Navigation Menu (☰) on the top left
   - Scroll down to **Storage** → Click **Cloud Storage** → **Buckets**

3. **Create New Bucket**:
   - Click **"CREATE BUCKET"** button
   - **Bucket name**: `data-warehouse-lab-deepb` (must be globally unique)
   - **Location type**: Region
   - **Location**: `us-east1`
   - **Storage class**: Standard (default)
   - **Access control**: Uniform (default)
   - Click **"CREATE"**

---

## Step 2: Create Folder Structure

1. **Open your bucket**:
   - Click on the bucket name `data-warehouse-lab-deepb`

2. **Create a data folder**:
   - Click **"CREATE FOLDER"** button
   - Name: `data`
   - Click **"CREATE"**

This creates an organized structure for storing datasets.

---

## Step 3: Upload Dataset

1. **Navigate to the data folder**:
   - Click on the `data` folder you just created

2. **Upload your CSV file**:
   - Click **"UPLOAD FILES"** button
   - Select your dataset file: `olist_customers_dataset.csv`
   - Wait for upload to complete
   - Verify the file appears in the folder

### Dataset Information:
- **File**: `olist_customers_dataset.csv`
- **Format**: CSV
- **Rows**: 99,441
- **Columns**: 5
  - `customer_id` (String)
  - `customer_unique_id` (String)
  - `customer_zip_code_prefix` (Integer)
  - `customer_city` (String)
  - `customer_state` (String)

---

## Step 4: Enable Object Versioning

Object versioning allows you to keep track of multiple versions of your files, useful for data recovery and audit trails.

### Enable Versioning:

1. **Navigate to bucket details**:
   - Go back to the main bucket view (click bucket name in breadcrumb)

2. **Enable versioning**:
   - Look for **"Object versioning"** section
   - If available, toggle it to **"ON"**
   - This ensures previous versions are retained when files are updated

✅ **Status**: Object versioning is now enabled for data recovery.

---

## Bucket Structure

After completion, your bucket structure should look like:

```
data-warehouse-lab-deepb/
└── data/
    └── olist_customers_dataset.csv
```

---

## Verification

### Verify Your Setup:

1. **Bucket created**: ✅ `data-warehouse-lab-deepb`
2. **Folder created**: ✅ `data/`
3. **Dataset uploaded**: ✅ `olist_customers_dataset.csv` (99,441 rows)
4. **Versioning enabled**: ✅ Object versioning ON

---

## Command Line Alternative (Using gsutil)

If you prefer command-line tools, you can achieve the same results using `gsutil`:

```bash
# Create bucket
gsutil mb -l us-east1 gs://data-warehouse-lab-deepb

# Create folder and upload file
gsutil cp olist_customers_dataset.csv gs://data-warehouse-lab-deepb/data/olist_customers_dataset.csv

# Enable versioning
gsutil versioning set on gs://data-warehouse-lab-deepb

# Verify upload
gsutil ls gs://data-warehouse-lab-deepb/data/
```