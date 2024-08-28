import unittest
import sys
import os
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from htmlnode import HTMLNode 
from blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_newlines(self) -> None:
        md: str = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here

* This is a list
* with items

> This is a quote
> on multiple lines

```
This is a code block
```
"""
        blocks: List[str] = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here",
                "* This is a list\n* with items",
                "> This is a quote\n> on multiple lines",
                "```\nThis is a code block\n```",
            ],
        )


class TestMarkdownBlockType(unittest.TestCase):

    def test_heading(self) -> None:
        self.assertEqual(block_to_block_type("# This is a heading"), "heading")
        self.assertEqual(block_to_block_type("## Subheading"), "heading")
        self.assertEqual(block_to_block_type("### Another heading"), "heading")

    def test_code_block(self) -> None:
        self.assertEqual(block_to_block_type("```\ncode block\n```"), "code")
        self.assertEqual(block_to_block_type(
            "```python\nprint('Hello, World!')\n```"), "code")

    def test_quote(self) -> None:
        self.assertEqual(block_to_block_type(
            "> This is a quote\n> It spans multiple lines"), "quote")
        self.assertEqual(block_to_block_type("> Single line quote"), "quote")

    def test_unordered_list(self) -> None:
        self.assertEqual(block_to_block_type(
            "* Item 1\n* Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type(
            "- Item 1\n- Item 2"), "unordered_list")

    def test_ordered_list(self) -> None:
        self.assertEqual(block_to_block_type(
            "1. First item\n2. Second item"), "ordered_list")
        self.assertEqual(block_to_block_type(
            "1. Item 1\n2. Item 2\n3. Item 3"), "ordered_list")

    def test_paragraph(self) -> None:
        self.assertEqual(block_to_block_type(
            "This is a simple paragraph."), "paragraph")
        self.assertEqual(block_to_block_type(
            "This is another paragraph.\nIt spans multiple lines."), "paragraph")

    def test_empty_block(self) -> None:
        self.assertEqual(block_to_block_type(""), "paragraph")


class TestMarkdownToHTML(unittest.TestCase):

    def test_paragraph(self) -> None:
        md: str = """This is **bolded** paragraph
text in a p
tag here

"""
        node: HTMLNode = markdown_to_html_node(md)
        html: str = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self) -> None:
        md: str = """This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
        node: HTMLNode = markdown_to_html_node(md)
        html: str = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self) -> None:
        md: str = """- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
        node: HTMLNode = markdown_to_html_node(md)
        html: str = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self) -> None:
        md: str = """# this is an h1

this is paragraph text

## this is an h2
"""
        node: HTMLNode = markdown_to_html_node(md)
        html: str = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self) -> None:
        md: str = """> This is a
> blockquote block

this is paragraph text

"""
        node: HTMLNode = markdown_to_html_node(md)
        html: str = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()
