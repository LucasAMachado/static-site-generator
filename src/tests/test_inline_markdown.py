import unittest
import sys
import os
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)
from inline_markdown import split_nodes_delimiter



class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self) -> None:
        node: TextNode = TextNode(
            "This is text with a **bolded** word", text_type_text)
        new_nodes: List[TextNode] = split_nodes_delimiter(
            [node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self) -> None:
        node: TextNode = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes: List[TextNode] = split_nodes_delimiter(
            [node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self) -> None:
        node: TextNode = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes: List[TextNode] = split_nodes_delimiter(
            [node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self) -> None:
        node: TextNode = TextNode(
            "This is text with an *italic* word", text_type_text)
        new_nodes: List[TextNode] = split_nodes_delimiter(
            [node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self) -> None:
        node: TextNode = TextNode("**bold** and *italic*", text_type_text)
        new_nodes: List[TextNode] = split_nodes_delimiter(
            [node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )

    def test_delim_code(self) -> None:
        node: TextNode = TextNode(
            "This is text with a `code block` word", text_type_text)
        new_nodes: List[TextNode] = split_nodes_delimiter(
            [node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
