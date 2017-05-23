from bs4 import BeautifulSoup
from urllib.request import urlopen
from model.item import Item
from helper import change_single_to_double_quotes

class CrawlerFeed():
    def __init__(self, url):
        self.url = url
        self.feed = BeautifulSoup(urlopen(self.url).read(), "xml")
        self.root = self.feed.find('channel')

    @property
    def items(self):
        return [Item(tag) for tag in self.root.findAll('item')]

    def parse_items(self):
        return [change_single_to_double_quotes('"item": {}'.format(item.parse()))
                for item in self.items]

    def build_json(self):
        return '{{"feed":[ {} ]}}'.format(",".join(self.describe_items()).replace("'", '"'))
