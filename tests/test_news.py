from lib.models.news import News

"""
News article constucts
"""
def test_news_constructs():
    news = News(1, "Test Title", "Test Content", "Test Publish_Date", "Test Image_URL")
    assert news.id == 1
    assert news.title == "Test Title"
    assert news.content == "Test Content"
    assert news.publish_date == "Test Publish_Date"
    assert news.image_url == "Test Image_URL"


"""
We can format news article to strings nicely
"""
def test_news_format_nicely():
    news = News(1, "Test Title", "Test Content", "Test Publish_Date", "Test Image_URL")
    assert str(news) == "News(1, 'Test Title', 'Test Content', 'Test Publish_Date', 'Test Image_URL')"
    

"""
We can compare two identical news articles
And have them be equal
"""
def test_news_are_equal():
    news1 = News(1, "Test Title", "Test Content", "Test Publish_Date", "Test Image_URL")
    news2 = News(1, "Test Title", "Test Content", "Test Publish_Date", "Test Image_URL")
    assert news1 == news2
   
"""
News article posts snippet
"""

def test_news_snippet():
    content = (
        "The position of the B.E.F had now become critical. As a result of a "
        "most skillfully conducted retreat and German errors, the bulk of the "
        "British Forces reached the Dunkirk bridgehead."
    )
    news = News(1, "Test Title", content, "Test Publish_Date", "Test Image_URL")
    assert news.get_snippet() == "The position of the B.E.F had now become critical...."
    