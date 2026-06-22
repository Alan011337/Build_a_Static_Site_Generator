import unittest
from block_to_block_type import block_to_block_type
from block_type import BlockType


class TestBlocktoBlockType(unittest.TestCase):
    def test_block_to_paragraph(self):
        block = "I will become a billionaire."
        block_type = block_to_block_type(block)
        block_answer = BlockType.PARAGRAPH
        self.assertEqual(block_type, block_answer)
    
    def test_block_to_heading(self):
        block = "# I will become a billionaire."
        block_type = block_to_block_type(block)
        block_answer = BlockType.HEADING
        self.assertEqual(block_type, block_answer)
        
    def test_block_to_code(self):
        block = "```\nI will become a billionaire.```"
        block_type = block_to_block_type(block)
        block_answer = BlockType.CODE
        self.assertEqual(block_type, block_answer)
        
    def test_block_to_quote(self):
        block = "> I will become a billionaire."
        block_type = block_to_block_type(block)
        block_answer = BlockType.QUOTE
        self.assertEqual(block_type, block_answer)
        
    def test_block_to_unordered_list(self):
        block = "- I will become a billionaire."
        block_type = block_to_block_type(block)
        block_answer = BlockType.UNORDERED_LIST
        self.assertEqual(block_type, block_answer)
    
    def test_block_to_ordered_list(self):
        block = "1. I will become a billionaire."
        block_type = block_to_block_type(block)
        block_answer = BlockType.ORDERED_LIST
        self.assertEqual(block_type, block_answer)