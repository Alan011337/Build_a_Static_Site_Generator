import unittest
from extract_title import extract_title


class test_extract_title(unittest.TestCase):
    def test1(self):
        extracted_title = extract_title("# Hello")
        expected_title = "Hello"
        self.assertEqual(extracted_title, expected_title)
        