import unittest

from leafnode import LeafNode, HTMLLeafType


class TestHTMLNode(unittest.TestCase):    
    def test_diff(self):
        node = LeafNode(HTMLLeafType.ITALIC, "These words have emphasis.")
        node2 = LeafNode(HTMLLeafType.ITALIC, "These words have emphasis.")
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode(HTMLLeafType.PARAGRAPH, "Hello, world!")
        self.assertEqual(node.toHTML(), "<p>Hello, world!</p>")

    def test_leaf_to_html_img(self):
        node = LeafNode(HTMLLeafType.IMAGE, "Pretty Picture", "banana.jpg")
        self.assertEqual(node.toHTML(), '<img src="banana.jpg" alt="Pretty Picture" />')

    def test_leaf_to_html_link(self):
        node = LeafNode(HTMLLeafType.LINK, "Go Here", "boot.dev")
        self.assertEqual(node.toHTML(), '<a href="boot.dev">Go Here</a>')

if __name__ == "__main__":
    unittest.main()