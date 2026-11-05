import unittest
from parentnode import *
from leafnode import *


class TestParentNode(unittest.TestCase):
    def test_parent_default_none_value(self):
        node = ParentNode("p", [LeafNode("b", "Bold text")])
        self.assertEqual(node.value, None)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),      
            "<div><span>child</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiplegreatgrandchildren(self):
        greatgrandchild_node1 = LeafNode("b", "grandchild#1 the Bold")
        greatgrandchild_node2 = LeafNode("i", "grandchild#2 the Italian")
        grandchild_node = ParentNode(
            "span", 
            [
                greatgrandchild_node1, 
                greatgrandchild_node2
            ]
        )
        child_node1 = ParentNode("span", [grandchild_node])
        child_node2 = LeafNode(
            "a", 
            "Click me!", 
            {"href": "https://www.google.com"}
        )
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            (
                '<div>'
                    '<span>'
                        '<span>'
                            '<b>'
                                'grandchild#1 the Bold'
                            '</b>'
                            '<i>'
                                'grandchild#2 the Italian'
                            '</i>'
                        '</span>'
                    '</span>'
                    '<a href="https://www.google.com">'
                        'Click me!'
                    '</a>'
                '</div>'
            )
        )


if __name__ == "__main__":
    unittest.main()