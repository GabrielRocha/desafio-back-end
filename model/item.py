
class Item:
    def __init__(self, tag):
        self.title = tag.find('title').text
        self.link = tag.find('link').text
        self.description = tag.find('title').text

    def parse(self):
        return dict(title=self.title,
                    link=self.link,
                    description=self.description)
