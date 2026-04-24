class Report:
    name = None

    def filter(self, rows):
        #Фильтрует строки по условию отчета
        raise NotImplementedError('Error: Each report must implement a filter')

    def headers(self):
        #Заголовки
        return ['title', 'ctr', 'retention_rate']

    def format_row(self, row):
        #Преобразование строк в формат для отчета
        return [row['title'], row['ctr'], row['retention_rate']]

class ClickbaitReport(Report):
    name = 'clickbait'

    def filter(self, rows):
        #Фильтрует ctr > 15 и retention_rate < 40
        result = []
        for row in rows:
            try:
                ctr = float(row['ctr'])
                retention = float(row['retention_rate'])
                if ctr > 15 and retention < 40:
                    result.append(row)
            except (ValueError, KeyError):
                #Некорректные строки
                continue
        return result

REPORTS = {'clickbait': ClickbaitReport,}

def get_report(report_name):
    #Возвращает отчет по report_name
    if report_name not in REPORTS:
        raise ValueError(f'Error: Unknown report {report_name}. Available reports: {list(REPORTS.keys())} ')
    return REPORTS[report_name]()