class Report:

    def __init__(self, id, title, reporting_year, report_type, file_url, is_public):
        self.id = id
        self.title = title 
        self.reporting_year = reporting_year
        self.report_type = report_type
        self.file_url = file_url
        self.is_public = is_public

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Report({self.id}, '{self.title}', '{self.reporting_year}', '{self.report_type}', '{self.file_url}', '{self.is_public}')"