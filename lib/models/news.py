class News:

    def __init__(self, id, title, content, publish_date, image_url):
        self.id = id
        self.title = title 
        self.content = content
        self.publish_date = publish_date
        self.image_url = image_url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"News({self.id}, '{self.title}', '{self.content}', '{self.publish_date}', '{self.image_url}')"
    
    # In news.py
    def get_snippet(self):
        if len(self.content) > 50:
            return self.content[:50] + "..."
        return self.content