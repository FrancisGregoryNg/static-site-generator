import unittest

from src.generate_page import *


class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello"
        title = extract_title(markdown)
        self.assertEqual(title, "Hello")

    def test_extract_title_with_space(self):
        markdown = "\n #  Hi"
        title = extract_title(markdown)
        self.assertEqual(title, "Hi")