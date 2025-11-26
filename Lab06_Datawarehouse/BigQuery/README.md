# Lab 06 - Part 2: Data Warehousing using Google BigQuery

## Overview
This lab demonstrates how to use Google BigQuery as a serverless data warehouse to analyze large datasets. You'll learn how to create datasets, load data from Google Cloud Storage, and run SQL queries for data analysis.

---

## What is Google BigQuery?
Google BigQuery is a fully-managed, serverless data warehouse solution by Google Cloud. It allows you to store and analyze massive datasets efficiently using SQL queries. BigQuery is designed to handle large-scale data analytics and can process billions of rows in just seconds, without requiring any infrastructure management.

---

## Lab Objectives
- Enable BigQuery API in Google Cloud Console
- Create a BigQuery dataset
- Load data from GCS into BigQuery tables
- Run SQL queries to analyze customer data
- Understand data warehousing concepts

---

## Prerequisites
- Completed Part 1: GCS Bucket setup
- Dataset uploaded to GCS bucket: `data-warehouse-lab-deepb/data/olist_customers_dataset.csv`
- Active GCP project with billing enabled
- Basic understanding of SQL

---

## Step 1: Enable BigQuery API

### Access BigQuery:

1. **Navigate to Google Cloud Console**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Ensure you're in the correct project

2. **Open BigQuery**:
   - Click the Navigation Menu (☰) on the top left
   - Scroll down to **"Big Data"** section
   - Click **"BigQuery"**

3. **Enable API** (if prompted):
   - If this is your first time using BigQuery, you may see an "Enable API" prompt
   - Click **"ENABLE"** to activate BigQuery API
   - Wait for activation to complete

✅ **Result**: BigQuery workspace opens with Explorer pane on the left

---

## Step 2: Create a BigQuery Dataset

A dataset in BigQuery is a container that holds tables and views. Think of it as a database.

### Create Dataset:

1. **In the BigQuery Explorer pane** (left side):
   - Locate your project name
   - Hover over your project name
   - Click the **three dots (⋮)** that appear
   - Select **"Create dataset"**

2. **Configure dataset**:
   - **Dataset ID**: `data_warehouse_lab`
   - **Data location**: `us-east1` (same region as your GCS bucket)
   - **Default table expiration**: Leave as "Never"
   - **Enable table expiration**: Leave unchecked
   - Keep other settings as default

3. **Create**:
   - Click **"CREATE DATASET"**

✅ **Result**: Dataset `data_warehouse_lab` appears under your project in the Explorer pane

---

## Step 3: Create Table and Load Data from GCS

Now let's create a table and populate it with data from your GCS bucket.

### Load Data into BigQuery:

1. **Click "CREATE TABLE"** button (top right, blue button)

2. **Configure Source**:
   - **Create table from**: Select **"Google Cloud Storage"**
   - **Select file from GCS bucket**: Enter the full path:
     ```
     data-warehouse-lab-deepb/data/olist_customers_dataset.csv
     ```
   - **File format**: Select **"CSV"**

3. **Configure Destination**:
   - **Project**: Auto-filled (your project name)
   - **Dataset**: `data_warehouse_lab` (should auto-populate)
   - **Table**: `customers`
   - **Table type**: Native table (default)

4. **Configure Schema**:
   - **Auto detect**: ✅ Check this box
   - BigQuery will automatically detect column names and data types from your CSV

5. **Advanced Options** (optional):
   - **Header rows to skip**: 1 (automatically set for CSV with headers)
   - Leave other settings as default

6. **Create Table**:
   - Click **"CREATE TABLE"** button at the bottom
   - Wait for the job to complete (usually takes a few seconds)

✅ **Result**: Table `customers` is created with 99,441 rows loaded

---

## Step 4: Verify Data Load

### Check Table Schema:

1. **Click on the `customers` table** in the Explorer pane
2. **View the Schema tab**:

Your table should have these columns:
- `customer_id` (STRING)
- `customer_unique_id` (STRING)
- `customer_zip_code_prefix` (INTEGER)
- `customer_city` (STRING)
- `customer_state` (STRING)

### Preview the Data:

3. **Click the "Preview" tab**:
   - View the first 50 rows of data
   - Verify data loaded correctly
   - Check for any data quality issues

✅ **Verification**: All 99,441 rows loaded successfully with correct schema

---

## Step 5: Query Data with SQL

Now for the exciting part - analyzing your data using SQL queries!

### Run Your First Query:

1. **Click the "Query" button** (blue button at the top)
2. **SQL editor opens** - this is where you write queries

---

### Query 1: Basic SELECT - View First 1000 Rows

```sql
SELECT * 
FROM `github-actions-lab-478523.data_warehouse_lab.customers` 
LIMIT 1000;
```

**What this does**: Retrieves all columns for the first 1000 customer records

**Result**: Displays customer IDs, zip codes, cities, and states

---

### Query 2: Count Customers by State

```sql
SELECT 
  customer_state,
  COUNT(*) as customer_count
FROM `github-actions-lab-478523.data_warehouse_lab.customers`
GROUP BY customer_state
ORDER BY customer_count DESC;
```

**What this does**: 
- Groups customers by state
- Counts how many customers are in each state
- Orders results from highest to lowest count

**Business Insight**: Identifies which Brazilian states have the most customers, useful for:
- Regional marketing strategies
- Distribution center planning
- Sales territory optimization

---

### Query 3: Top 10 Cities with Most Customers

```sql
SELECT 
  customer_city,
  customer_state,
  COUNT(*) as customer_count
FROM `github-actions-lab-478523.data_warehouse_lab.customers`
GROUP BY customer_city, customer_state
ORDER BY customer_count DESC
LIMIT 10;
```

**What this does**:
- Groups customers by city and state
- Shows the top 10 cities with most customers
- Includes state information for context

**Business Insight**: Helps identify major urban markets for:
- Targeted advertising campaigns
- Local partnerships
- Same-day delivery feasibility

---

### Query 4: Analyze Unique Customers vs Total Records

```sql
SELECT 
  COUNT(DISTINCT customer_unique_id) as unique_customers,
  COUNT(*) as total_records
FROM `github-actions-lab-478523.data_warehouse_lab.customers`;
```

**What this does**:
- Counts unique customers using `customer_unique_id`
- Counts total records in the table
- Compares the two numbers

**Business Insight**: 
- If unique_customers < total_records, some customers have multiple entries
- Helps understand repeat customer behavior
- Important for customer lifetime value analysis

---

## Query Execution

### How to Run Queries:

1. **Copy the SQL query** into the editor
2. **Replace project ID** if needed:
   - Change `github-actions-lab-478523` to your actual project ID
3. **Click "RUN"** button (blue button)
4. **View results** in the Results tab below

### Understanding Results:

- **Query completed**: Green checkmark appears
- **Job information**: Shows data processed and execution time
- **Results tab**: Displays query output in a table
- **Execution details**: Shows bytes processed and slot time used

---

## SQL Query Patterns Explained

### Basic Syntax:
```sql
SELECT [columns]
FROM [project].[dataset].[table]
WHERE [conditions]
GROUP BY [grouping columns]
ORDER BY [sorting column]
LIMIT [number of rows];
```

### Common Functions:
- `COUNT(*)`: Count all rows
- `COUNT(DISTINCT column)`: Count unique values
- `SUM(column)`: Add up numeric values
- `AVG(column)`: Calculate average
- `MAX(column)`, `MIN(column)`: Find highest/lowest values

### Aggregation:
- Use `GROUP BY` to summarize data by categories
- Use `ORDER BY` to sort results
- Use `LIMIT` to restrict number of rows returned