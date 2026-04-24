import csv

def read_csv_file(file_paths):
    all_rows = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding = 'utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    all_rows.append(row)
        except FileNotFoundError:
            raise FileNotFoundError(f'Error: File {file_path} not found')
        except Exception as e:
            raise Exception(f'Error: reading file {file_path}: {e}')
    return all_rows

