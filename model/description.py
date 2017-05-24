from bs4 import BeautifulSoup
from util import parse_tag


class Description:
    def __init__(self, tag):
        self.html = BeautifulSoup(tag.text, "html.parser")

    def parse(self):
        return parse_tag(self.html)
