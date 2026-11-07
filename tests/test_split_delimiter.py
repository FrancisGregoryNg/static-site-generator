import unittest

from src.split_delimiter import *
from src.textnode import *


class TestSplitDelimiter(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode(
            "This is text with a **bold block** word", 
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_split_italic(self):
        node = TextNode(
            "This is text with an _italic block_ word", 
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_split_code(self):
        node = TextNode(
                "This is text with a `code block` word", 
                TextType.TEXT,
            )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_bold_start(self):
        node = TextNode(
            "**Bold start** is good", 
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("Bold start", TextType.BOLD),
            TextNode(" is good", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_italic_ends(self):
        node = TextNode(
            "_Italian_ is also _italic_", 
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("Italian", TextType.ITALIC),
            TextNode(" is also ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ]
        self.assertEqual(new_nodes, expected_nodes) 

    def test_split_code_sequential(self):
        node = TextNode(
                "Look at these codes: `code block 1``code block 2`", 
                TextType.TEXT,
            )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("Look at these codes: ", TextType.TEXT),
            TextNode("code block 1", TextType.CODE),
            TextNode("code block 2", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected_nodes)   

    def test_multiple_old_nodes(self):
        node1 = TextNode(
            "This is text with a **bold block** word", 
            TextType.TEXT,
        )
        node2 = TextNode(
            "**Bold start** is good", 
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("Bold start", TextType.BOLD),
            TextNode(" is good", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)      