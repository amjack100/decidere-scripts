## Prerequisites

1. Install the Google Cloud libraries:

```bash
pip install google-cloud-bigquery google-cloud-storage
```

2. Authenticate with ADC:
 
```bash
gcloud auth application-default login
```

## Usage

```bash
python export_table_to_csv.py \
  --project    my-gcp-project \
  --dataset    my_dataset \
  --table      my_table \
  --bucket     my_bucket_name \
  --blob       exports/my_table.csv \
  --output     local_copy.csv```
```