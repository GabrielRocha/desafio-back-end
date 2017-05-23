from bs4 import BeautifulSoup

class Description:
    def __init__(self, tag):
        self.html = BeautifulSoup(tag.text, "html.parser")

    def parse_tag_p(self):
        return [tag_p.text.strip() for tag_p in self.html.findAll('p') if tag_p.text.strip()]
