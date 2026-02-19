import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_false_heading(self):
        block= "####### This is a false heading."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_real_heading(self):
        block= "## This is a real heading."
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_quote(self):
        block= ">To write good test\n> you first must know the answer"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_false_quote(self):
        block= ">To write good test\n you first must know the answer"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_real_ordered_list(self):
        block ="1. This should work\n2. as a list\n3. I hope"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
    
    def test_false_ordered_list(self):
        block="1. This list should fail\n1.For multiple reasons"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_real_unordered_list(self):
        block="- hopefully i understand\n- the rules for an unordered\n- list"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_false_unordered_list(self):
        block="-this list should fail"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_false_unordered_list_again(self):
        block="- This list should fail too\n For a different reason"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_code_block(self):
        block = "```\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_false_code_block_missing_closing(self):
        block = "```\nprint('hi')\n"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_false_code_block_no_newline_after_ticks(self):
        # spec says it must start with ``` and a newline
        block = "```print('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading_requires_space(self):
        block = "##This should not be a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading_level_6_is_valid(self):
        block = "###### Level 6 heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_ordered_list_must_increment(self):
        block = "1. one\n3. three"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_must_start_at_1(self):
        block = "2. two\n3. three"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph_default(self):
        block = "Just a normal paragraph\nwith two lines."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
