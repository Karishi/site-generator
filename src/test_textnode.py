import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_diff(self):
        node = TextNode("Testing...", TextType.IMAGE)
        node2 = TextNode("Testing...", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_var(self):
        node = TextNode("Testing...", TextType.IMAGE)
        node2 = TextNode("Testing...", TextType.IMAGE, "boot.dev")
        self.assertNotEqual(node, node2)

    def test_url_same(self):
        node = TextNode("Testing...", TextType.IMAGE, "boot.dev")
        node2 = TextNode("Testing...", TextType.IMAGE, "boot.dev")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()