def change_single_to_double_quotes(string):
    return string.replace("'", '"')


def flatten_list(list_with_list):
    _list = []
    for element in list_with_list:
        if type(element) == list:
            _list += element
        else:
            _list.append(element)
    return _list


def parse_p(p):
    text = p.text.strip()
    if text:
        return dict(type='text', content=text)


def parse_img(img):
    src = img.attrs.get('src', None)
    if src:
        return dict(type='image', content=src)


def parse_ul(ul):
    href = [li.find('a').attrs.get('href', "").strip()
            for li in ul.findAll('li') if li.find('a')]
    if href:
        return dict(type='links', content=href)


def parse_div(div):
    result = [TAGS.get(children.name)(children)
              for children in div.children
              if children.name in TAGS]
    return result


TAGS = dict(p=parse_p,
            img=parse_img,
            ul=parse_ul,
            div=parse_div)
