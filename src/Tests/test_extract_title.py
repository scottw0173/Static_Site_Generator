import unittest

from extracting_markdown import extract_title  # <-- change to your module name


class TestExtractTitle(unittest.TestCase):
    def test_single_h1_simple(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_h1_with_extra_whitespace(self):
        md = "#    Hello World   "
        self.assertEqual(extract_title(md), "Hello World")

    def test_h1_in_multiline_markdown(self):
        md = """
# My Title

This is a paragraph.

## Subtitle

More text.
"""
        self.assertEqual(extract_title(md), "My Title")

    def test_ignores_h2_and_h3(self):
        md = """
## Not the title

### Also not the title

# The Real Title
"""
        self.assertEqual(extract_title(md), "The Real Title")

    def test_title_not_first_line(self):
        md = """
Some intro text

# Actual Title

More text
"""
        self.assertEqual(extract_title(md), "Actual Title")

    def test_raises_if_no_h1(self):
        md = """
## Subtitle only

Paragraph text

### Another subtitle
"""
        with self.assertRaises(Exception):
            extract_title(md)

    def test_ignores_lines_starting_with_multiple_hashes(self):
        md = "## Not a title\n### Still not\n# Yes this is"
        self.assertEqual(extract_title(md), "Yes this is")

    def test_hash_without_space_not_h1(self):
        md = "#Title without space\n# Proper Title"
        # Depending on your implementation choice:
        # If you require "# " (hash + space), this should return "Proper Title"
        self.assertEqual(extract_title(md), "Proper Title")


if __name__ == "__main__":
    unittest.main()