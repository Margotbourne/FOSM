from lib.models.news import News
from lib.repositories.news_repository import NewsRepository

def test_get_all_news(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = NewsRepository(db_connection)
    assert len(repo.all()) == 2

def test_create_news(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = NewsRepository(db_connection)
    repo.create(News(None, "New Grant", "Details", "2026-02-11", "img.jpg"))
    assert len(repo.all()) == 3

def test_delete_news(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = NewsRepository(db_connection)
    repo.delete(1)
    assert len(repo.all()) == 1