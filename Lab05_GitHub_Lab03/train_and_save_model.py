import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from google.cloud import storage
import joblib
import json
from datetime import datetime

# Download necessary data - Iris data from sklearn library
# We define a function to download the data
def download_data():
  from sklearn.datasets import load_wine
  wine = load_wine()
  features = pd.DataFrame(wine.data, columns=wine.feature_names)
  target = pd.Series(wine.target)
  return features, target

# Define a function to preprocess the data
# In this case, preprocessing will be just splitting the data into training and testing sets
def preprocess_data(X, y):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  return X_train, X_test, y_train, y_test

# Define a function to train the model
def train_model(X_train, y_train):
  model = RandomForestClassifier(n_estimators=100, random_state=42)
  model.fit(X_train, y_train)
  return model

# Define a function to save the model both locally and in GCS
def save_model_to_gcs(model, bucket_name, blob_name):
  joblib.dump(model, "model.joblib")
  
  # Save the model to GCS
  storage_client = storage.Client()
  bucket = storage_client.bucket(bucket_name)
  blob = bucket.blob(blob_name)
  blob.upload_from_filename('model.joblib')

# Define a function to save metrics to GCS
def save_metrics_to_gcs(metrics, bucket_name, blob_name):
  # Save metrics locally as JSON
  with open('metrics.json', 'w') as f:
    json.dump(metrics, f, indent=4)
  
  # Upload to GCS
  storage_client = storage.Client()
  bucket = storage_client.bucket(bucket_name)
  blob = bucket.blob(blob_name)
  blob.upload_from_filename('metrics.json')
  print(f"Metrics saved to gs://{bucket_name}/{blob_name}")
  
# Putting all functions together
def main():
  # Download data
  X, y = download_data()
  X_train, X_test, y_train, y_test = preprocess_data(X, y)
  
  # Train model
  model = train_model(X_train, y_train)
  
  # Evaluate model
  y_pred = model.predict(X_test)
  accuracy = accuracy_score(y_test, y_pred)
  precision = precision_score(y_test, y_pred, average='weighted')
  recall = recall_score(y_test, y_pred, average='weighted')
  f1 = f1_score(y_test, y_pred, average='weighted')
  
  print(f'Model Accuracy: {accuracy:.4f}')
  print(f'Model Precision: {precision:.4f}')
  print(f'Model Recall: {recall:.4f}')
  print(f'Model F1-Score: {f1:.4f}')
  
  # Save the model to gcs
  bucket_name = "lab05-github-actions"
  timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
  blob_name = f"trained_models/model_{timestamp}.joblib"
  save_model_to_gcs(model, bucket_name, blob_name)
  print(f"Model saved to gs://{bucket_name}/{blob_name}")
  
  # Create metrics dictionary
  metrics = {
    'accuracy': float(accuracy),
    'precision': float(precision),
    'recall': float(recall),
    'f1_score': float(f1),
    'timestamp': datetime.now().isoformat(),
    'model_type': 'RandomForestClassifier',
    'dataset': 'Wine'
  }
  
  # Save metrics to GCS
  metrics_blob_name = f"metrics/metrics_{timestamp}.json"
  save_metrics_to_gcs(metrics, bucket_name, metrics_blob_name)
  
if __name__ == "__main__":
  main()