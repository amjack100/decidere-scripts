import csv

input_file = 'input.csv'  # Replace with your CSV file path
output_file = 'id_to_name.csv'  # Output file name

# Open the input CSV file for reading
with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)

    # Open the output CSV file for writing
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        # Specify the columns to write in the new file
        fieldnames = ['ID', 'Index Name']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Write the header row to the output file
        writer.writeheader()

        # Iterate over each row in the input file and write only the desired columns
        for row in reader:
            # Append the suffix "-0" to the ID
            modified_id = row['ID'] + '-0'
            writer.writerow({
                'ID': modified_id,
                'Index Name': row['Index Name']
            })