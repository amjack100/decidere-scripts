
import base64
from google.cloud import bigquery
import pandas as pd
from datetime import date, timedelta
import math
import os



    # Decode base64 string


    # Save to a temporary JSON file
    temp_credentials_path = '/tmp/gcp_credentials.json'
    with open(temp_credentials_path, 'w') as f:
        f.write(credentials_json)

    # Set environment variable
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = temp_credentials_path

# df = pd.read_csv('reshaped_file.csv')



# Authenticate with the base64 credentials



def wipe_calc_data_table():
    client = bigquery.Client()
    table_id = "decidere.bx_index.calc_data"

    # Option 1: Using DELETE to remove all rows.
    query = f"DELETE FROM `{table_id}` WHERE TRUE"

    # Alternatively, if TRUNCATE is available for your table, you can use:
    # query = f"TRUNCATE TABLE `{table_id}`"

    query_job = client.query(query)
    query_job.result()  # Wait for the query to complete
    print(f"All rows from {table_id} have been deleted.")


def compute_return(curr, past):
    """Compute simple return given current and past values."""
    if past in (None, 0) or (isinstance(past, float) and math.isnan(past)):
        return None
    return curr / past - 1


def compute_annualized_return(curr, past, years):
    """Compute annualized return over a multi-year period."""
    if past in (None, 0) or (isinstance(past, float) and math.isnan(past)):
        return None
    return math.pow(curr / past, 1 / years) - 1


def get_value(sub_df, target):
    # Filter for dates less than or equal to target.
    available = sub_df[sub_df['date'] <= target]
    if available.empty:
        return None
    # Return the value from the most recent available date.
    return available.sort_values('date', ascending=False).iloc[0]['value']

def get_first_available_value_itd(sub_df):
    valid = sub_df[sub_df['value'].notnull()].sort_values('date', ascending=True)
    if valid.empty:
        return None
    return valid.iloc[0]['value']

def calculate_and_insert_returns():
    # Initialize BigQuery client
    client = bigquery.Client()

    mapping_df = pd.read_csv("id_to_name.csv")  # CSV with columns: id, name
    id_to_name = mapping_df.set_index("id")["name"].to_dict()

    # Pull the data from bx_push_data
    query = """
    SELECT id, time, value
    FROM `decidere.bx_index.bx_push_data`
    """
    df = client.query(query).to_dataframe()

    # Convert 'time' (DATETIME) to a date for easier filtering.
    df['date'] = pd.to_datetime(df['time']).dt.date

    # Use yesterday as the target date since data is always one day behind.
    target_date = date.today() - timedelta(days=1)

    results = []

    # Loop over each unique id (56 unique items expected)
    for unique_id in df['id'].unique():
        sub_df = df[df['id'] == unique_id]

        # Find the "current" row for this id (target_date)
        curr_df = sub_df[sub_df['date'] == target_date]
        if curr_df.empty:
            print(f"No data available for id {unique_id} on {target_date}")
            continue

        curr_row = curr_df.iloc[0]
        curr_value = curr_row['value']

        # Helper to get value for a specific date for the current id

            # row = sub_df[sub_df['date'] == target]
            # return row.iloc[0]['value'] if not row.empty else None

        value_7day = get_value(sub_df, target_date - timedelta(days=7))
        value_30day = get_value(sub_df, target_date - timedelta(days=30))
        value_3mo = get_value(sub_df, target_date - timedelta(days=90))  # Approximation for 3 months
        value_ytd = get_value(sub_df, date(target_date.year, 1, 1))
        value_1yr = get_value(sub_df, target_date - timedelta(days=365))
        value_3yr = get_value(sub_df, target_date - timedelta(days=3 * 365))
        value_5yr = get_value(sub_df, target_date - timedelta(days=5 * 365))
        value_itd = get_first_available_value_itd(sub_df)

        result = {
            'id': unique_id,
            'name': id_to_name.get(unique_id, unique_id),  # Look up the name, fallback to id if not found
            'return_7day': compute_return(curr_value, value_7day),
            'return_30day': compute_return(curr_value, value_30day),
            'return_3mo': compute_return(curr_value, value_3mo),
            'return_ytd': compute_return(curr_value, value_ytd),
            'return_1yr': compute_return(curr_value, value_1yr),
            'return_3yr_ann_': compute_annualized_return(curr_value, value_3yr, 3) if value_3yr is not None else None,
            'return_5yr_ann_': compute_annualized_return(curr_value, value_5yr, 5) if value_5yr is not None else None,
            'return_itd': compute_return(curr_value, value_itd)
        }
        results.append(result)

    if not results:
        print("No results to insert.")
        return

    # Insert all calculated rows into calc_data table.
    table_id = "decidere.bx_index.calc_data"
    print(results)
    errors = client.insert_rows_json(table_id, results)
    if errors:
        print("Encountered errors:", errors)
    else:
        print(f"Inserted {len(results)} rows successfully.")


if __name__ == "__main__":
    calculate_and_insert_returns()
