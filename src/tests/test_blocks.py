import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from blocks import markdown_to_blocks
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


if __name__ == "__main__":
    unittest.main()
