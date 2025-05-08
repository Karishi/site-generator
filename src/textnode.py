from enum import Enum
from leafnode import LeafNode, HTMLLeafType

class TextType(Enum):
    TEXT = "text"
    BOLD = "**bold**"
    ITALIC = "_italic_"
    CODE = "`code`"
    LINK = "[link anchor text](url)"
    IMAGE = "![image alt text](url)"

class TextNode():
    def __init__(self, text, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.BOLD:
        output = LeafNode(HTMLLeafType.BOLD, text_node.text)
    elif text_node.text_type == TextType.TEXT:
        output = LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.IMAGE:
        output = LeafNode(HTMLLeafType.IMAGE, text_node.text, text_node.url)
    elif text_node.text_type == TextType.ITALIC:
        output = LeafNode(HTMLLeafType.ITALIC, text_node.text)
    elif text_node.text_type == TextType.CODE:
        output = LeafNode(HTMLLeafType.CODE, text_node.text)
    elif text_node.text_type == TextType.LINK:
        output = LeafNode(HTMLLeafType.LINK, text_node.text, text_node.url)
    else:
        raise Exception("Invalid text type.")
    return output
    