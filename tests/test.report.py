from lib.models.report import Report

"""
Report article constucts
"""
def test_report_constructs():
    report = Report(1, "Test Title", "Test Reporting_Year", "Test Report_Type", "Test File_URL", "Test Is_Public")
    assert report.id == 1
    assert report.title == "Test Title"
    assert report.reporting_year == "Test Reporting_Year"
    assert report.report_type == "Test Report_Type"
    assert report.file_url == "Test File_URL"
    assert report.is_public == "Test Is_Public"


"""
We can format report article to strings nicely
"""
def test_report_format_nicely():
    report = Report(1, "Test Title", "Test Reporting_Year", "Test Report_Type", "Test File_URL", "Test Is_Public")
    assert str(report) == "Report(1, 'Test Title', 'Test Reporting_Year', 'Test Report_Type', 'Test File_URL', 'Test Is_Public')"

"""
We can compare two identical report articles
And have them be equal
"""
def test_report_are_equal():
    report1 = Report(1, "Test Title", "Test Reporting_Year", "Test Report_Type", "Test File_URL", "Test Is_Public")
    report2 = Report(1, "Test Title", "Test Reporting_Year", "Test Report_Type", "Test File_URL", "Test Is_Public")
    assert report1 == report2
   