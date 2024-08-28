import unittest
import sys
import os
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_image,
    text_type_link,
)
from split_links_and_images import split_nodes_image, split_nodes_link



class TestSplitNodesImage(unittest.TestCase):
    def test_general_result(self) -> None:
        node: TextNode = TextNode(
            "This is text with an image ![boot logo](https://www.boot.dev/logo.png) and another image ![youtube logo](https://www.youtube.com/logo.png)",
            text_type_text,
        )
        new_nodes: List[TextNode] = split_nodes_image([node])
        expected_nodes: List[TextNode] = [
            TextNode("This is text with an image ", text_type_text, None),
            TextNode("boot logo", text_type_image,
                     "https://www.boot.dev/logo.png"),
            TextNode(" and another image ", text_type_text, None),
            TextNode("youtube logo", text_type_image,
                     "https://www.youtube.com/logo.png"),
        ]
        self.assertEqual(new_nodes, expected_nodes)


class TestSplitNodesLink(unittest.TestCase):
    def test_general_result(self) -> None:
        node: TextNode = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        new_nodes: List[TextNode] = split_nodes_link([node])
        expected_nodes: List[TextNode] = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode("to youtube", text_type_link,
                     "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(new_nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()
