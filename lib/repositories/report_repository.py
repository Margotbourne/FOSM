from lib.models.report import Report

class ReportRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM report')
        reports = [] 
        for row in rows:
            item = Report(
                row["id"], row["title"], row["reporting_year"], 
                row["report_type"], row["file_url"], 
                row["is_public"]
            )
            reports.append(item)
        return reports

    def find(self, report_id):
        rows = self._connection.execute('SELECT * FROM report WHERE id = %s', [report_id])
        if not rows: return None
        row = rows[0]
        return Report(row["id"], row["title"], row["reporting_year"], row["report_type"], row["file_url"], row["is_public"])

    def create(self, report):
        self._connection.execute(
            'INSERT INTO report (title, reporting_year, report_type, file_url, is_public) VALUES (%s, %s, %s, %s, %s)',
            [report.title, report.reporting_year, report.report_type, report.file_url, report.is_public]
        )
        return None

    def delete(self, report_id):
        self._connection.execute('DELETE FROM report WHERE id = %s', [report_id])
        return None