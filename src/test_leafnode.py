import unittest

from leafnode import *


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_result = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected_result)

    def test_leaf_to_html_link(self):
        node = LeafNode(
            "a", 
            "Click me!", 
            {"href": "https://www.google.com"}
        )
        expected_result = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_result)

    def test_leaf_default_none_child(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.children, None)

if __name__ == "__main__":
    unittest.main()