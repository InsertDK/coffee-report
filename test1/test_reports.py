import pytest
from reports import ClickbaitReport, get_report

def test_clickbait_video_valid():
    #Позитивный сценарий теста
    #Проверка видео ctr > 15 retention_rate < 40
    report = ClickbaitReport()
    video = [
        {'title': 'video1', 'ctr': '25.5', 'retention_rate': '30.5'}
    ]
    result = report.filter(video)
    #Проверяю, что в отчет попало подходящее видео
    assert len(result) == 1
    #Проверяю, что в отчет упало нужное видео
    assert result[0]['title'] == 'video1'

def test_clickbait_video_invalid():
    #Негативный сценарий теста
    report = ClickbaitReport()
    video = [
        {'title': 'video2', 'ctr': '10.5', 'retention_rate': '60.5'}
    ]
    result = report.filter(video)
    assert len(result) == 0

def test_get_report_clickbait():
    #Проверка get_report возвращает отчет 'clickbait'
    report = get_report('clickbait')
    #Проверяет, что report является объектом класса ClickbaitReport.
    assert isinstance(report, ClickbaitReport)
    assert report.name == 'clickbait'

def test_get_report_error():
    #Проверяю выпадет ли ошибка при неизвестном отчете
    with pytest.raises(ValueError):
        report = get_report('unknown_report')
