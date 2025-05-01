import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)
    
    def test_diff(self):
        node = TextNode("Testing...", TextType.image)
        node2 = TextNode("Testing...", TextType.italic)
        self.assertNotEqual(node, node2)

    def test_url_var(self):
        node = TextNode("Testing...", TextType.image)
        node2 = TextNode("Testing...", TextType.image, "boot.dev")
        self.assertNotEqual(node, node2)

    def test_url_same(self):
        node = TextNode("Testing...", TextType.image, "boot.dev")
        node2 = TextNode("Testing...", TextType.image, "boot.dev")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()