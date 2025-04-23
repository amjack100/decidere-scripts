import os
import base64
import json
from google.cloud import bigquery, storage



    # Decode base64 string


    # Save to a temporary JSON file
    temp_credentials_path = '/tmp/gcp_credentials.json'
    with open(temp_credentials_path, 'w') as f:
        f.write(credentials_json)

    # Set environment variable
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = temp_credentials_path


# Your base64 encoded credentials string

def export_table_to_csv(project_id, dataset_id, table_id, bucket_name, destination_blob_name):


    # Authenticate with the base64 credentials

    # Initialize BigQuery and GCS clients
    bq_client = bigquery.Client()
    gcs_client = storage.Client()

    # Set table and GCS bucket paths
    destination_uri = f"gs://{bucket_name}/{destination_blob_name}"
    dataset_ref = bq_client.dataset(dataset_id, project=project_id)
    table_ref = dataset_ref.table(table_id)

    # Configure job to export BigQuery data as a CSV
    extract_job = bq_client.extract_table(
        table_ref,
        destination_uri,
        location="US",  # Update if your dataset is in another location
    )

    # Wait for the export job to complete
    extract_job.result()

    # Download file from GCS
    bucket = gcs_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.download_to_filename("your_local_filename.csv")

    print("Exported table to CSV and downloaded to your local file.")


# Example usage
export_table_to_csv("decidere", "Demo_DB_Football", "2024_Sample_v3", "decidere-1", "Demo_DB_Football.csv")
