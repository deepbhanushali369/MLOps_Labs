# Lab 06: Data Storage and Warehousing using Google Cloud Platform (GCP)

## 🎯 Lab Overview

This lab provides hands-on experience with cloud-based data storage and warehousing using Google Cloud Platform (GCP). You'll learn how to store data in Google Cloud Storage (GCS) and analyze it using Google BigQuery, two fundamental services for modern data engineering and analytics workflows.

---

## 🎓 Learning Objectives

By completing this lab, you will:
- Set up scalable cloud storage using Google Cloud Storage
- Organize and manage datasets in GCS buckets
- Create and configure a BigQuery data warehouse
- Load data from GCS into BigQuery tables
- Write and execute SQL queries for data analysis
- Understand the integration between storage and compute layers
- Apply best practices for cloud data management

---

## 📊 Lab Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Lab 06 Architecture                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Local Dataset (CSV)                                         │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────────────┐                                   │
│  │  Google Cloud Storage │  ◄── Part 1: Buckets             │
│  │  (GCS Bucket)         │                                   │
│  │  - data-warehouse-lab │                                   │
│  │  - 99,441 rows        │                                   │
│  └──────────┬────────────┘                                   │
│             │                                                │
│             │ Data Loading                                   │
│             ▼                                                │
│  ┌──────────────────────┐                                   │
│  │   Google BigQuery     │  ◄── Part 2: BigQuery            │
│  │   (Data Warehouse)    │                                   │
│  │  - SQL Analytics      │                                   │
│  │  - Business Insights  │                                   │
│  └───────────────────────┘                                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗂️ Lab Structure

This lab is divided into two main components:

```
LAB06_DATAWAREHOUSE/
│
├── README.md (this file - main overview)
│
├── BigQuery/
│   ├── README.md (detailed BigQuery guide)
│   ├── Loaded_Customer_Table_in_BigQuery.png
│   ├── Preview_Customer_Table.png
│   ├── SQL Query 01.png
│   ├── SQL Query 02.png
│   └── SQL Query 03.png
│
└── Buckets/
    ├── README.md (detailed GCS guide)
    ├── Bucket_Created.png
    ├── Data_added_inside_Bucket.png
    └── olist_customers_dataset.csv
```

### Part 1: Buckets (Google Cloud Storage)
**Location**: `Buckets/` folder

Focuses on:
- Creating GCS buckets for data storage
- Uploading datasets to cloud storage
- Enabling versioning for data recovery
- Organizing data with folder structures

**Key Deliverable**: Dataset stored in GCS at `data-warehouse-lab-deepb/data/olist_customers_dataset.csv`

### Part 2: BigQuery (Data Warehouse)
**Location**: `BigQuery/` folder

Focuses on:
- Setting up BigQuery datasets and tables
- Loading data from GCS into BigQuery
- Writing SQL queries for data analysis
- Extracting business insights from data

**Key Deliverable**: Fully functional data warehouse with analytical queries

---

## 🚀 Getting Started

### Prerequisites

Before starting this lab, ensure you have:
- ✅ Active Google Cloud Platform (GCP) account
- ✅ GCP project with billing enabled
- ✅ Basic understanding of SQL (helpful but not required)
- ✅ Dataset ready for analysis (CSV format)

### Recommended Sequence

Follow these steps in order:

1. **Start with Part 1: Buckets**
   - Read `Buckets/README.md`
   - Create GCS bucket
   - Upload your dataset
   - Enable versioning

2. **Continue with Part 2: BigQuery**
   - Read `BigQuery/README.md`
   - Enable BigQuery API
   - Create dataset and table
   - Load data from GCS
   - Run SQL queries

---

## 📦 Dataset Information

### Dataset: Olist Customer Data

This lab uses the Olist Brazilian E-Commerce dataset, specifically the customer information:

- **File**: `olist_customers_dataset.csv`
- **Size**: 99,441 rows
- **Columns**: 5
  - `customer_id` - Unique identifier for each transaction
  - `customer_unique_id` - Unique identifier for each customer
  - `customer_zip_code_prefix` - First 5 digits of customer zip code
  - `customer_city` - Customer city name
  - `customer_state` - Customer state (Brazilian state codes)

**Source**: Olist Brazilian E-Commerce Public Dataset

---

## 🔧 Technologies Used

### Google Cloud Storage (GCS)
- **Purpose**: Scalable object storage for datasets
- **Benefits**: 
  - Durable and highly available
  - Integrates with BigQuery
  - Supports versioning and lifecycle management
  - Cost-effective for large datasets

### Google BigQuery
- **Purpose**: Serverless data warehouse for analytics
- **Benefits**:
  - Process billions of rows in seconds
  - No infrastructure management required
  - SQL-based queries (familiar to most analysts)
  - Built-in machine learning capabilities
  - Pay only for data processed

---

## 💡 Key Concepts

### Data Lake vs Data Warehouse

**Data Lake (GCS)**:
- Raw data storage
- Flexible schema
- Lower cost per GB
- Good for long-term retention

**Data Warehouse (BigQuery)**:
- Structured, processed data
- Optimized for queries
- Fast analytics performance
- Good for business intelligence

### Why Use Both?

1. **Separation of Storage and Compute**: Store data cheaply in GCS, analyze on-demand in BigQuery
2. **Flexibility**: Keep raw data in GCS while creating multiple BigQuery tables for different analyses
3. **Cost Optimization**: Pay for BigQuery only when running queries
4. **Scalability**: Both services scale automatically to handle any data size

---

## 📈 Lab Results

### Infrastructure Created

✅ **Google Cloud Storage**:
- Bucket: `data-warehouse-lab-deepb`
- Region: `us-east1`
- Folder: `data/`
- Dataset: `olist_customers_dataset.csv` (99,441 rows)
- Features: Object versioning enabled

✅ **BigQuery**:
- Dataset: `data_warehouse_lab`
- Table: `customers`
- Schema: 5 columns (auto-detected)
- Data: 99,441 rows loaded successfully

### Analytics Performed

✅ **SQL Queries Executed**:
1. Basic data exploration (SELECT with LIMIT)
2. Customer distribution by state (GROUP BY state)
3. Top 10 cities analysis (GROUP BY city)
4. Unique customer count (COUNT DISTINCT)

### Business Insights Gained

- Identified states with highest customer concentration
- Discovered top cities for targeted marketing
- Analyzed unique vs. repeat customer patterns
- Established foundation for deeper customer analytics