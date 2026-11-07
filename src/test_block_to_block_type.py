import unittest

from block_to_block_type import *


class TestBlockToBlocktype(unittest.TestCase):
    def test_heading(self):
        block = "###### Heading level 6"
        blocktype = block_to_block_type(block)

        self.assertEqual(blocktype, BlockType.HEADING)
    def test_code(self):
        block = (
            "```\n"
            "print('Hello world!')"
            "```"
        )
        blocktype = block_to_block_type(block)

        self.assertEqual(blocktype, BlockType.CODE)
    def test_quote(self):
        block = (
            ">I am sleepy\n"
            "> - Me"
        )
        blocktype = block_to_block_type(block)

        self.assertEqual(blocktype, BlockType.QUOTE)
    def test_unordered_list(self):
        block = (
            "- This is a list\n"
            "- with items\n"
            "- and more items"
        )
        blocktype = block_to_block_type(block)

        self.assertEqual(blocktype, BlockType.UNORDERED_LIST)
    def test_ordered_list(self):
        block = (
            "1. Item 1\n"
            "2. Item 2\n"
            "3. Item 3\n"
            "4. Item 4\n"
            "5. Item 5\n"
            "6. Item 6\n"
            "7. Item 7\n"
            "8. Item 8\n"
            "9. Item 9\n"
            "10. Item 10"
        )
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = (
             "This is another paragraph with _italic_ text and `code` here\n"
             "This is the same paragraph on a new line"
        )
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)
                