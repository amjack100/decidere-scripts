#!/usr/bin/env python3
import argparse
from google.cloud import bigquery, storage

def export_table_to_csv(
    project_id: str,
    dataset_id: str,
    table_id: str,
    bucket_name: str,
    destination_blob_name: str,
    local_filename: str
):
    """
    Extract a BigQuery table to GCS as CSV, then download it locally.
    Relies on Application Default Credentials.
    """
    # Clients will pick up ADC from your environment (gcloud auth application-default login)
    bq_client = bigquery.Client(project=project_id)
    gcs_client = storage.Client(project=project_id)

    # 1) export to GCS
    destination_uri = f"gs://{bucket_name}/{destination_blob_name}"
    dataset_ref = bq_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    extract_job = bq_client.extract_table(
        table_ref,
        destination_uri,
        location="US",
    )
    extract_job.result()  # wait

    # 2) download from GCS
    bucket = gcs_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.download_to_filename(local_filename)

    print(f"Exported {project_id}.{dataset_id}.{table_id} → {local_filename}")


def main():
    p = argparse.ArgumentParser(
        description="Export a BigQuery table as CSV via GCS (using ADC)."
    )
    p.add_argument("--project",  required=True, help="GCP project ID")
    p.add_argument("--dataset",  required=True, help="BigQuery dataset ID")
    p.add_argument("--table",    required=True, help="BigQuery table ID")
    p.add_argument("--bucket",   required=True, help="GCS bucket name")
    p.add_argument("--blob",     required=True,
                   help="GCS object name (e.g. folder/table_export.csv)")
    p.add_argument("--output",   required=True, help="Local CSV filename")
    args = p.parse_args()

    export_table_to_csv(
        project_id=args.project,
        dataset_id=args.dataset,
        table_id=args.table,
        bucket_name=args.bucket,
        destination_blob_name=args.blob,
        local_filename=args.output,
    )


if __name__ == "__main__":
    main()
