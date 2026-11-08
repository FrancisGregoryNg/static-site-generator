import unittest

from src.markdown_to_html_node import *


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            (
                "<div>"
                    "<p>"
                        "This is "
                        "<b>"
                            "bolded"
                        "</b>"
                        " paragraph text in a p tag here"
                    "</p>"
                    "<p>"
                        "This is another paragraph with "
                        "<i>"
                            "italic"
                        "</i>"
                        " text and "
                        "<code>"
                            "code"
                        "</code>"
                        " here"
                    "</p>"
                "</div>"
            )
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            (
                "<div>"
                    "<pre>"
                        "<code>"
                            "This is text that _should_ remain\n"
                            "the **same** even with inline stuff\n"
                        "</code>"
                    "</pre>"
                "</div>"
            )

        )

    def test_heading(self):
        md = """
#### Header Level **4**: very _important_ `code`.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            (
                "<div>"
                    "<h4>"
                        "Header Level "
                        "<b>"
                            "4"
                        "</b>"
                        ": very "
                        "<i>"
                            "important"
                        "</i>"
                        " "
                        "<code>"
                            "code"
                        "</code>"
                        "."
                    "</h4>"
                "</div>"
            )
        )

    def test_quote(self):
        md = """
> I am very tired
> This is very true indeed
> I need to sleep soon
>_- from my haiku collection_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            (
                "<div>"
                    "<blockquote>"
                        "I am very tired\n"
                        "This is very true indeed\n"
                        "I need to sleep soon\n"
                        "<i>"
                            "- from my haiku collection"
                        "</i>"
                    "</blockquote>"
                "</div>"
            )
        )

    def test_unordered_list(self):
        md = """
- drink **water**
- eat _healthy_
- be happy
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            (
                "<div>"
                    "<ul>"
                        "<li>"
                            "drink "
                            "<b>"
                                "water"
                            "</b>"
                        "</li>"
                        "<li>"
                            "eat "
                            "<i>"
                                "healthy"
                            "</i>"
                        "</li>"
                        "<li>"
                            "be happy"
                        "</li>"
                    "</ul>"
                "</div>"
            )
        )

    def test_ordered_list(self):
        md = """
1. **General**
2. _Lieutenant_ General
3. _Major_ General
4. _Brigadier_ General
5. Colonel
6. Lieutenant Colonel
7. Major
8. Captain
9. First Lieutenant
10. Second Lieutenant
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            (
                "<div>"
                    "<ol>"
                        "<li>"
                            "<b>"
                                "General"
                            "</b>"
                        "</li>"
                        "<li>"
                            "<i>"
                                "Lieutenant"
                            "</i>"
                            " General"
                        "</li>"
                        "<li>"
                            "<i>"
                                "Major"
                            "</i>"     
                            " General"
                        "</li>"
                        "<li>"
                            "<i>"
                                "Brigadier"
                            "</i>"
                            " General"
                        "</li>"
                        "<li>"
                            "Colonel"
                        "</li>"
                        "<li>"
                            "Lieutenant Colonel"
                        "</li>"
                        "<li>"
                            "Major"
                        "</li>"
                        "<li>"
                            "Captain"
                        "</li>"
                        "<li>"
                            "First Lieutenant"
                        "</li>"
                        "<li>"
                            "Second Lieutenant"
                        "</li>"
                    "</ol>"
                "</div>"
            )
        )