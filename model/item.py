from .description import Description
from util import convert_to_double_quotes


class Item:
    def __init__(self, tag):
        self.title = tag.find('title').text
        self.link = tag.find('link').text
        self.description = Description(tag.find('description'))

    def parse(self):
        result = dict(title=self.title, link=self.link,
                      description=self.description)
        return convert_to_double_quotes('"item": {}'.format(result))

    def __repr__(self):
        return self.title
