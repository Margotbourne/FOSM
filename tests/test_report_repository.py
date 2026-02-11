from lib.models.report import Report
from lib.repositories.report_repository import ReportRepository

def test_get_all_reports(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ReportRepository(db_connection)
    assert len(repo.all()) == 2

def test_create_report(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ReportRepository(db_connection)
    repo.create(Report(None, "Report 2026", 2026, "Annual", "url", True))
    assert len(repo.all()) == 3

def test_delete_report(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ReportRepository(db_connection)
    repo.delete(1)
    assert len(repo.all()) == 1