# Decidere Scripts

This repository contains various standalone Python scripts used to support the Decidere project.

## Scripts

| Script | Description |
|:-------|:------------|
| `combine_ms_data.py` | Combines Morningstar data files into a single consolidated dataset. |
| `compute_and_load_bx_returns.py` | Computes benchmark returns and loads them into a BigQuery table. |
| `export_table_to_csv.py` | Exports a BigQuery table to a CSV file in Google Cloud Storage and optionally downloads a local copy. |


## Setup

Some scripts require Google Cloud setup to run successfully. For `export_table_to_csv.py` and `compute_and_load_bx_returns.py`, make sure you have:

1. Installed the necessary Google Cloud libraries:

    ```bash
    pip install google-cloud-bigquery google-cloud-storage
    ```

2. Authenticated with Application Default Credentials (ADC):

    ```bash
    gcloud auth application-default login
    ```

If other scripts require setup, add instructions here as needed.

## Usage

### `export_table_to_csv.py`

Run:

```bash
python scripts/export_table_to_csv.py \
  --project    my-gcp-project \
  --dataset    my_dataset \
  --table      my_table \
  --bucket     my_bucket_name \
  --blob       exports/my_table.csv \
  --output     local_copy.csv
```

### `combine_ms_data.py`

Combines Morningstar data files into a single dataset.

Run:

```bash
python scripts/combine_ms_data.py
```

*(Modify the script if needed to point to local data files.)*

### `compute_and_load_bx_returns.py`

Computes benchmark returns and uploads them to BigQuery.

Run:

```bash
python scripts/compute_and_load_bx_returns.py
```

*(Ensure environment is authenticated with Google Cloud if writing to BigQuery.)*