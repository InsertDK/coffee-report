import argparse
from tabulate import tabulate
from utils import read_csv_file
from reports import get_report

def parse_arguments():
    #Парсит аргументы
    parser = argparse.ArgumentParser(description = 'Analysis of video metrics on YouTube')
    parser.add_argument('--files', nargs = '+', required = True, help = 'Path on CSV files')
    parser.add_argument('--report', required = True, help = 'Name report (clickbait)')
    return parser.parse_args()

def print_report(data, report):
    #Выводит отчет в виде таблицы
    if not data:
        print('There is no data matching the report conditions')
        return

    #Сортируем по ctr на убывание
    sorted_data = sorted(data, key = lambda x: float(x['ctr']), reverse = True)

    #Вывод таблицы
    table_data = [report.format_row(row) for row in sorted_data]
    print(tabulate(table_data, headers = report.headers(), tablefmt = 'grid'))

def main():
        args = parse_arguments()
        all_rows = read_csv_file(args.files)

        try:
            report = get_report(args.report)
        except ValueError as e:
            print(f'Error: {e}')
            return 1

        filtered_rows = report.filter(all_rows)

        print_report(filtered_rows, report)

        return 0

if __name__ == '__main__':
    exit(main())

