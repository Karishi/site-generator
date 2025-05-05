from enum import Enum
from htmlnode import HTMLNode
from leafnode import LeafNode

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



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        self.tag = tag
        self.props = props
        self.children = children
        super().__init__(tag, children = self.children, props = self.props)

    def toHTML(self):
        if not self.tag:
            raise ValueError("All parent nodes must include a tag.")
        elif not self.children:
            raise ValueError("All parent nodes must include children.")
        else:
            output = self.tag.value[0]
            for child in self.children:
                if child.children:
                    output += child.toHTML()
                else:
                    if child.tag:
                        output += child.tag.value[0]
                    output += child.value
                    if child.tag:
                        output += child.tag.value[1]
            output += self.tag.value[1]
            return output

        
# node = ParentNode(
#     HTMLLeafType.PARAGRAPH,
#     [
#         LeafNode(HTMLLeafType.BOLD, "Bold text"),
#         LeafNode(None, "Normal text"),
#         LeafNode(HTMLLeafType.ITALIC, "italic text"),
#         LeafNode(None, "Normal text"),
#     ],
# )



# node = node.toHTML()
# print(node)