import unittest

from src.textnode import *
from src.split_markdown_to_textnode import *


class TestSplitMarkdownToTextNode(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            (
                "This is text with an"
                " ![image](https://i.imgur.com/zjjcJKZ.png) "
                "and another ![second image](https://i.imgur.com/3elNhQu.png)"
            ),
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "image", 
                    TextType.IMAGE, 
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", 
                    TextType.IMAGE, 
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
        )

    def test_split_link(self):
        node = TextNode(
            (
                "This is text with a link [to boot dev](https://www.boot.dev)"
                " and [to youtube](https://www.youtube.com/@bootdotdev)"
            ),
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode(
                    "to boot dev", 
                    TextType.LINK, 
                    "https://www.boot.dev",
                ),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", 
                    TextType.LINK, 
                    "https://www.youtube.com/@bootdotdev",
                ),
            ],
        )

    def test_split_images_start_text_end(self):
        node = TextNode(
            (
                "![This image](https://i.imgur.com/zjjcJKZ.png) "
                "is better than ![this other image]"
                "(https://i.imgur.com/3elNhQu.png), in my opinion."
            ),
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode(
                    "This image", 
                    TextType.IMAGE, 
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
                TextNode(" is better than ", TextType.TEXT),
                TextNode(
                    "this other image", 
                    TextType.IMAGE, 
                    "https://i.imgur.com/3elNhQu.png",
                ),
                TextNode(", in my opinion.", TextType.TEXT),
            ],
        )