import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_trims_whitespace_each_block(self):
        md = "  # Heading  \n\n   Paragraph   "
        self.assertEqual(markdown_to_blocks(md), ["# Heading", "Paragraph"])

    def test_removes_empty_blocks_from_extra_newlines(self):
        md = "Para1\n\n\n\nPara2\n\n\n\n\nPara3"
        self.assertEqual(markdown_to_blocks(md), ["Para1", "Para2", "Para3"])

    def test_single_block(self):
        md = "Just one block"
        self.assertEqual(markdown_to_blocks(md), ["Just one block"])

if __name__ == "__main__":
    unittest.main()