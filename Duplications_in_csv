import pandas as pd
import os

def find_duplicates_in_csv(directory, output_file):
    # Check if directory exists
    if not os.path.exists(directory):
        print(f'Directory "{directory}" does not exist.')
        return

    all_duplicates = []  # List to hold duplicates from all files

    # Loop through each file in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            print(f'\nChecking for duplicates in {filename}...')

            try:
                # Read the CSV file into a DataFrame
                df = pd.read_csv(file_path)

                # Check for duplicates
                duplicates = df[df.duplicated()]

                if not duplicates.empty:
                    print(f'Duplicates found in {filename}')
                    # Add a column to indicate the source file of the duplicates
                    duplicates['source_file'] = filename
                    all_duplicates.append(duplicates)  # Store the duplicates
                else:
                    print(f'No duplicates found in {filename}.')
                    
            except Exception as e:
                print(f"An error occurred with file {filename}: {e}")

    # Combine all duplicates into one DataFrame
    if all_duplicates:
        combined_duplicates = pd.concat(all_duplicates, ignore_index=True)

        # Save combined duplicates to a new CSV file
        combined_duplicates.to_csv(output_file, index=False)
        print(f'\nAll duplicates have been saved to {output_file}')
    else:
        print('No duplicates found in any of the files.')

# Specify the directory containing your CSV files and the output CSV file
directory_path = 'folder/folder'  # Update with the correct path
output_csv = 'duplicates_output.csv'  # Name for the output file
find_duplicates_in_csv(directory_path, output_csv)
