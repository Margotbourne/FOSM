class GalleryPhoto:
    def __init__(self, id, title, caption, filename, upload_date=None):
        self.id = id
        self.title = title
        self.caption = caption
        self.filename = filename
        self.upload_date = upload_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"GalleryPhoto({self.id}, {self.title}, {self.filename})"