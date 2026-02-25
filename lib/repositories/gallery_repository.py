from lib.models.gallery import GalleryPhoto

class GalleryRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM gallery ORDER BY id DESC")
        galleryphotos = []
        for row in rows:
            galleryphoto=GalleryPhoto(row["id"], row["title"], row["caption"], row["filename"], row["upload_date"])
            galleryphotos.append(galleryphoto)
        return galleryphotos
    
    def add(self, photo):
        self._connection.execute(
            "INSERT INTO gallery (title, caption, filename) VALUES (%s, %s, %s)",
            [photo.title, photo.caption, photo.filename]
        )

    def delete(self, galleryphoto_id):
        self._connection.execute('DELETE FROM gallery WHERE id = %s', [galleryphoto_id])
        return None

