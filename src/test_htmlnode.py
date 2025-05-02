import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):    
    def test_diff(self):
        node = HTMLNode("html", "https://www.google.com", None, {"href": "https://www.yahoo.com", "target": "_blank",})
        node2 = HTMLNode("html", "https://www.google.com", None, {"href": "https://www.google.com", "target": "_blank",})
        self.assertNotEqual(node, node2)

    def test_url_var(self):
        node = HTMLNode("html", "https://www.google.com", None, {"href": "https://www.google.com", "target": "_blank",})
        output = node.props_to_HTML()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()