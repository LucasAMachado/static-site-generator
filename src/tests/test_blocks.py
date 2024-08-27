import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from blocks import markdown_to_blocks, block_to_block_type
import unittest

class TestMarkdownToBlocks(unittest.TestCase):
    def test_multiple_markdown_blocks(self):
        markdown = '''
        # This is a heading
        
        This is a paragraph of text. It has some **bold** and *italic* words inside of it.
        
        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        '''

        result_blocks = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
                         '* This is the first list item in a list block\n* This is a list item\n* This is another list item']

        self.assertEqual(markdown_to_blocks(markdown.strip()), result_blocks)


class TestMarkdownBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("# This is a heading"), "heading")
        self.assertEqual(block_to_block_type("## Subheading"), "heading")
        self.assertEqual(block_to_block_type("### Another heading"), "heading")

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\ncode block\n```"), "code")
        self.assertEqual(block_to_block_type(
            "```python\nprint('Hello, World!')\n```"), "code")

    def test_quote(self):
        self.assertEqual(block_to_block_type(
            "> This is a quote\n> It spans multiple lines"), "quote")
        self.assertEqual(block_to_block_type("> Single line quote"), "quote")

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type(
            "* Item 1\n* Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type(
            "- Item 1\n- Item 2"), "unordered_list")

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type(
            "1. First item\n2. Second item"), "ordered_list")
        self.assertEqual(block_to_block_type(
            "1. Item 1\n2. Item 2\n3. Item 3"), "ordered_list")

    def test_paragraph(self):
        self.assertEqual(block_to_block_type(
            "This is a simple paragraph."), "paragraph")
        self.assertEqual(block_to_block_type(
            "This is another paragraph.\nIt spans multiple lines."), "paragraph")

    def test_empty_block(self):
        self.assertEqual(block_to_block_type(""), "paragraph")

if __name__ == "__main__":
    unittest.main()
