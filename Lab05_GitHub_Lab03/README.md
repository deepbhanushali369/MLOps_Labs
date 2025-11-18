# GitHub Actions and GCP Integration Lab

## 🎯 Overview
This project demonstrates automated machine learning workflows using **GitHub Actions** and **Google Cloud Platform (GCP)**. The workflow automatically trains a RandomForest classifier on the Wine dataset and saves both the trained model and performance metrics to Google Cloud Storage.

## 🚀 Features
- ✅ Automated ML model training using GitHub Actions
- ✅ Wine quality classification using RandomForestClassifier
- ✅ Comprehensive metrics tracking (Accuracy, Precision, Recall, F1-Score)
- ✅ Automatic model and metrics export to Google Cloud Storage
- ✅ Secure authentication with GCP service accounts
- ✅ Manual workflow triggering via GitHub Actions UI

## 📁 Project Structure
```
Lab05_GitHub_Lab03/
├── train_and_save_model.py    # Main training script
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

.github/
└── workflows/
    └── train-lab05.yaml        # GitHub Actions workflow
```

## 🛠️ Technologies Used
- **Python 3.10**
- **scikit-learn** - Machine Learning
- **pandas** - Data manipulation
- **Google Cloud Storage** - Model storage
- **GitHub Actions** - CI/CD automation
- **joblib** - Model serialization

## 📊 Dataset
**Wine Dataset** from scikit-learn
- 178 samples
- 13 features (chemical properties)
- 3 classes (wine cultivars)
- Classification task

### 1. Clone the Repository
```bash
git clone https://github.com/deepbhanushali369/MLOps_Labs.git
cd MLOps_Labs/Lab05_GitHub_Lab03
```

### 2. Set Up Google Cloud Platform

#### Create GCP Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project: `github-actions-lab`

#### Create Service Account
1. Navigate to **IAM & Admin** → **Service Accounts**
2. Create service account: `github-actions-sa`
3. Grant role: **Storage Admin**
4. Generate JSON key and download it

#### Create GCS Bucket
1. Go to **Cloud Storage** → **Buckets**
2. Create bucket: `lab05-github-actions`
3. Choose region close to you

### 3. Configure GitHub Secrets
1. Go to your GitHub repository
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Add new secret:
   - Name: `GCP_GITHUB_LAB05`
   - Value: Paste entire JSON key content

### 4. Run the Workflow
1. Go to **Actions** tab in GitHub
2. Select **"Train and save model to GCS"**
3. Click **"Run workflow"**
4. Wait for completion (2-3 minutes)

## 📈 Model Performance
The RandomForest model achieves the following metrics on the Wine dataset:
- **Accuracy:** 100%
- **Precision:** 100%
- **Recall:** 100%
- **F1-Score:** 100%

*Note: Perfect scores indicate the Wine dataset is relatively simple for RandomForest classification.*

## 📦 Outputs in GCS

### Trained Models
```
gs://lab05-github-actions/trained_models/
└── model_YYYYMMDDHHMMSS.joblib
```

### Performance Metrics
```
gs://lab05-github-actions/metrics/
└── metrics_YYYYMMDDHHMMSS.json
```

**Metrics JSON Format:**
```json
{
    "accuracy": 1.0,
    "precision": 1.0,
    "recall": 1.0,
    "f1_score": 1.0,
    "timestamp": "2025-11-18T00:33:02.557978",
    "model_type": "RandomForestClassifier",
    "dataset": "Wine"
}
```

## 🔄 Workflow Details

### Trigger
- **Manual:** Via GitHub Actions UI (`workflow_dispatch`)