from enum import Enum
from htmlnode import HTMLNode

class HTMLLeafType(Enum):
    PARAGRAPH = '<p>', '</p>'
    HEADING1 = '<h1>', '</h1>'
    HEADING2 = '<h2>', '</h2>'
    HEADING3 = '<h3>', '</h3>'
    HEADING4 = '<h4>', '</h4>'
    HEADING5 = '<h5>', '</h5>'
    HEADING6 = '<h6>', '</h6>'
    BOLD = '<b>', '</b>'
    ITALIC = '<i>', '</i>'
    LINK = '<a href="address">', '</a>'
    IMAGE = '<img src="url/of/image.jpg" alt="Description of image" />', ''
    LISTITEM = '<li>', '</li>'
    BLOCKQUOTE = '<blockquote>', '</blockquote>'
    CODE = '<code>', '</code>'



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=None)

    def toHTML(self):
        if not self.value:
            raise ValueError("All leaf nodes must include a value.")
        if not self.tag:
            return str(self.value())
        elif self.tag == HTMLLeafType.LINK:
            return f'<a href="{self.props}">{self.value}</a>'
        elif self.tag == HTMLLeafType.IMAGE:
            return f'<img src="{self.props}" alt="{self.value}" />'
        else:
            return f'{self.tag.value[0]}{self.value}{self.tag.value[1]}'