from lib.models.news import News

class NewsRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM news ORDER BY publish_date DESC')
        newses = [] 
        for row in rows:
            item = News(
                row["id"], row["title"], row["content"], 
                row["publish_date"], row["image_url"]
            )
            newses.append(item)
        return newses

    def find(self, news_id):
        rows = self._connection.execute('SELECT * FROM news WHERE id = %s', [news_id])
        if not rows: return None
        row = rows[0]
        return News(row["id"], row["title"], row["content"], row["publish_date"], row["image_url"])

    def create(self, news):
        self._connection.execute(
            'INSERT INTO news (title, content, publish_date, image_url) VALUES (%s, %s, %s, %s)',
            [news.title, news.content, news.publish_date, news.image_url]
        )
        return None

    def delete(self, news_id):
        self._connection.execute('DELETE FROM news WHERE id = %s', [news_id])
        return None