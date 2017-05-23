from .description import Description


class Item:
    def __init__(self, tag):
        self.title = tag.find('title').text
        self.link = tag.find('link').text
        self.description = Description(tag.find('description'))

    def parse(self):
        return dict(title=self.title,
                    link=self.link,
                    description=self.description)

    def __repr__(self):
        return self.title
