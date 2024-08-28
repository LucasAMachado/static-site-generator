import unittest
import sys
import os
from typing import Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_image,
    text_node_to_html_node
)
from htmlnode import LeafNode



class TestTextNode(unittest.TestCase):
    def test_eq(self) -> None:
        node: TextNode = TextNode('This is a text node', 'bold')
        node2: TextNode = TextNode('This is a text node', 'bold')
        self.assertEqual(node, node2)

    def test_not_eq_url(self) -> None:
        node: TextNode = TextNode('This is a text node', 'bold', None)
        node2: TextNode = TextNode('This is a text node', 'bold',
                                   'https://lucasamachado.com')
        self.assertNotEqual(node, node2)

    def test_not_eq_all(self) -> None:
        node: TextNode = TextNode('This is a text node.', 'bold.',
                                  "https://lucasamachado.com/test")
        node2: TextNode = TextNode('This is a text node', 'bold',
                                   'https://lucasamachado.com')
        self.assertNotEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self) -> None:
        node: TextNode = TextNode("This is a text node", text_type_text)
        html_node: LeafNode = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self) -> None:
        node: TextNode = TextNode("This is an image", text_type_image,
                                  "https://www.boot.dev")
        html_node: LeafNode = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self) -> None:
        node: TextNode = TextNode("This is bold", text_type_bold)
        html_node: LeafNode = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
