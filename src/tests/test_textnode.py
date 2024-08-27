import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest

from htmlnode import LeafNode

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_image,
    text_node_to_html_node
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('This is a text node', 'bold')
        node2 = TextNode('This is a text node', 'bold')

        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode('This is a text node', 'bold', None)
        node2 = TextNode('This is a text node', 'bold',
                         'https://lucasamachado.com')

        self.assertNotEqual(node, node2)

    def test_not_eq_all(self):
        node = TextNode('This is a text node.', 'bold.',
                        "https://lucasamachado.com/test")
        node2 = TextNode('This is a text node', 'bold',
                         'https://lucasamachado.com')

        self.assertNotEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", text_type_image,
                        "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", text_type_bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")



if __name__ == "__main__":
    unittest.main()
