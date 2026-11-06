import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        child_1 = HTMLNode(value="1")
        child_2 = HTMLNode(value="2")
        html_node_1 = HTMLNode(
            tag="p", 
            value="sample text", 
            children=[child_1, child_2], 
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        html_node_2 = HTMLNode(
            tag="p", 
            value="sample text", 
            children=[child_1, child_2], 
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(html_node_1, html_node_2)

    def test_default_values(self):
        html_node = HTMLNode()
        self.assertEqual(
            (
                html_node.tag, 
                html_node.value, 
                html_node.children, 
                html_node.props
            ),
            (None, None, None, None),
        )

    def test_props_to_html(self):
        html_node = HTMLNode(
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            html_node.props_to_html(), 
            ' href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html_if_none(self):
        html_node = HTMLNode(props = None)
        self.assertEqual(html_node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()