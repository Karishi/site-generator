import unittest
from leafnode import LeafNode, HTMLLeafType
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode(HTMLLeafType.HEADING1, "child")
        parent_node = ParentNode(HTMLLeafType.PARAGRAPH, [child_node])
        self.assertEqual(parent_node.toHTML(), "<p><h1>child</h1></p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode(HTMLLeafType.BOLD, "grandchild")
        child_node = ParentNode(HTMLLeafType.HEADING1, [grandchild_node])
        parent_node = ParentNode(HTMLLeafType.PARAGRAPH, [child_node])
        self.assertEqual(
            parent_node.toHTML(),
            "<p><h1><b>grandchild</b></h1></p>",
        )

if __name__ == "__main__":
    unittest.main()