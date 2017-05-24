from bs4 import BeautifulSoup
from util import convert_to_double_quotes, parse_tag


class Description:
    def __init__(self, tag):
        self.html = BeautifulSoup(tag.text, "html.parser")

    def parse(self):
        return convert_to_double_quotes("'description':{}"
                                        .format(parse_tag(self.html)))
