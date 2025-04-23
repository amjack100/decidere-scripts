# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import pandas as pd
import re

COLUMN_ROW_NUMBER = 10

def combine_files(directory, files,output_file):
    df_list = []
    print(f'Combining {len(files)} files')
    # Iterate through all the files in the directory
    expected_output_rows = []
    expected_columns = 0

    for i, file in enumerate(files):
        print(f'{i + 1} out of {len(files)}')
        # Skip files that are not Excel files
        header_row = 10
        if re.search(r'AMPF\sSelect\sStrategies', file):
            header_row = 10

        df = pd.read_excel(directory + file,header=header_row - 1)
        # df.columns = columns.columns
        print(file)
        print(f'{df.shape[0]} rows')
        expected_output_rows.append(df.shape[0])
        expected_columns = df.shape[1]

        for index, row in df.iterrows():
            if isinstance(row[0],str) and len(row[0]) == 10:
                df_list.append(row)

    print('-------------------')
    print(f'Expected shape: {sum(expected_output_rows)} rows, {expected_columns} columns')
    # Concatenate all the data frames into one big data frame
    df_big = pd.concat(df_list,axis=1).T
    print(f'Actual shape: {df_big.shape[0]} rows, {df_big.shape[1]} columns')
    print(f'Difference: {sum(expected_output_rows) - df_big.shape[0]} rows, {expected_columns - df_big.shape[1]} columns')

    # print(f'Actual output columns: {df_big.shape[1]}')

    df_big.to_csv(directory + output_file, index=False)

def main():
    # Set the directory where the Excel files are stored
    directory = '/home/andy/Documents/Morningstar-January-2025/'

    # Create an empty list to store the data frames
    excel_files = [file for file in os.listdir(directory) if file.endswith('.xlsx')]
    MF_files = [file for file in excel_files if re.match('^MF', file)]
    ETF_files = [file for file in excel_files if re.match('^ETF', file)]
    SMA_files = [file for file in excel_files if re.match('^SMA', file)]
    MS_Extract_files = MF_files + ETF_files + SMA_files
    EnvestnetPlus_files = [file for file in excel_files if re.search(r'Envestnet\sStrategies|AMPF\sSelect\sStrategies', file)]

    combine_files(directory, MF_files, '_MF.csv')
    combine_files(directory, ETF_files, '_ETF.csv')
    combine_files(directory, SMA_files, '_SMA.csv')
    combine_files(directory, EnvestnetPlus_files, '_EnvestnetPlus.csv')
    combine_files(directory, MS_Extract_files, '_MS_Extract.csv')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
