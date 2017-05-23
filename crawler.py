from lxml import etree
from model.item import Item
from helper import change_single_to_double_quotes

class CrawlerFeed():
    def __init__(self, url):
        self.url = url
        self.feed = etree.parse(self.url)
        self.root = self.feed.find('channel')

    @property
    def items(self):
        return self.root.findall('item')

    def parse_items(self):
        return [change_single_to_double_quotes('"item": {}'.format(Item(tag).parse()))
                for tag in self.items]
