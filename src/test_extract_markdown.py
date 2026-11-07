import unittest

from extract_markdown import *


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = (
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
            " and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        extracted_images = extract_markdown_images(text)
        self.assertEqual(
            extracted_images,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ]
        ) 

    def test_extract_markdown_links(self):
        text = (
            "This is text with a link [to boot dev](https://www.boot.dev)"
            " and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        extracted_links = extract_markdown_links(text)
        self.assertEqual(
            extracted_links,
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ]
        )

    def test_extract_markdown_image_not_link(self):
        text = (
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
            " and a link [to boot dev](https://www.boot.dev)."
        )
        extracted_images = extract_markdown_images(text)
        self.assertEqual(
            extracted_images,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ]
        ) 

    def test_extract_markdown_link_not_image(self):
        text = (
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
            " and a link [to boot dev](https://www.boot.dev)."
        )
        extracted_links = extract_markdown_links(text)
        self.assertEqual(
            extracted_links,
            [
                ("to boot dev", "https://www.boot.dev"),
            ]
        )   